let a = [
  '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
  '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
  //'[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
  //'[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]',
  //'[7,[5,[[3,8],[1,4]]]]',
  //'[[2,[2,2]],[8,[8,1]]]',
  //'[2,9]',
  //'[1,[[[9,3],9],[[9,0],[0,7]]]]',
  //'[[[5,[7,4]],7],1]',
  //'[[[[4,2],2],6],[8,7]]'
]

let xl, xr, x, s, stack = {
  arr: [],
  data: []
}

const explode = (a, level = 1) => {
  if (level === 1) {
    stack.arr = a
  }
	if (typeof a !== 'object') return a
  // if we meet the criteria, start the 'explosion'
  if (level == 5 && !x) {
  	x = true
  	xl = a[0]
    xr = a[1]
    console.log(stack)
    //let sl = stack.length -1

    // if we're on the left side of the parent
    // go up the right side and apply the r value
    // if (stack[sl][2] == 0) {
    //   v = stack[sl][1]
    //   while (typeof v !== 'number') v = v[0]
    //   v += xr
    //   xr = undefined
    // }
    
    return 0
  }
  // insert the right hand exploded value on the way up
  // if (xr && typeof a[0] === 'number') { 
  //  	a[0] += xr
  //  	xr = undefined
  // }
  // recurse
  stack.data.push([level, 0])
  let l = explode(a[0], level + 1)
  stack.data.pop()
  stack.data.push([level, 1])
  let r = explode(a[1], level + 1)
  stack.data.pop()
  //insert the left hand exploded value as we go down
  // if (typeof l === 'number') {
  // 	if (l === -1) l = 0
  //   else if (xl) {
  //    	//l += xl
  //     xl = undefined
  //   }
  // }
  //insert the right hand exploded value as we go down
  // if (typeof r === 'number') {
  // 	if (r === -1) r = 0
  //   else if (xr) {
  //    	r += xr
  //     xr = undefined
  //   }
  // }
  // if we reach the bottom and still have an exploded left hand value
  //if (p === undefined && xl) {
    // let v = l
    // while (typeof v[1] !== 'number') {
    //   v = v[1]
    // }
    // v[1] += xl
    //xl = undefined
  //}
  return [l, r]
}
const split = (a) => {
	if (typeof a === 'number') {
  	if (a >= 10 && !s) {
    	s = true
    	return [Math.floor(a/2),Math.ceil(a/2)]
    }
  	return a
  }
	return [split(a[0]), split(a[1])]
}
const reduce = (t) => {	
  function operate(t) {
    console.log('E > ', JSON.stringify(t))
    t = explode(t)
    if (x) {
      console.log('  < ', JSON.stringify(t))
      return t
    }
    t = split(t)
    if (s) {
      return t
    }
    return t
  }
	do {
    s = undefined
    x = undefined
    xl = undefined
    xr = undefined
    t = operate(t)
  } while (x || s)

  return t
}
const add = (a, b) => {
	return [a, b]
}
const mag = (a) => {
	if (typeof a !== 'object') return a
  return (3 * mag(a[0])) + (2 * mag(a[1]))
}

var t = JSON.parse('[[[[0,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]')
console.log(JSON.stringify(t))
t = explode(t)
console.log(JSON.stringify(t))
// let t = JSON.parse(a[0])
// for (let i = 1; i < a.length; i++) {
//   let t1 = JSON.parse(a[i])
//   t = add(t, t1)
//   t = reduce(t)
// }
// console.log(JSON.stringify(t))