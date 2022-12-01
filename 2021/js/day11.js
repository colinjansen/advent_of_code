const a = [
'2478668324',
'4283474125',
'1663463374',
'1738271323',
'4285744861',
'3551311515',
'8574335438',
'7843525826',
'1366237577',
'3554687226'
].map(l => [...l].map(n => +n))

let flashes = 0
let done = false
let step = 0

const flashers = []
  
const flash = (a) => {
	while (flashers.length) {
  	const f = flashers.pop()
    flashes++
    let m = [ 
    	[f[0] + 1, f[1] - 1], 
      [f[0] + 1, f[1]], 
      [f[0] + 1, f[1] + 1], 
      [f[0] - 1, f[1] - 1], 
      [f[0] - 1, f[1]], 
      [f[0] - 1, f[1] + 1], 
      [f[0], f[1] + 1], 
      [f[0], f[1] - 1]
    ]
    while (m.length) {
      const c = m.pop()
      if (a[c[0]] !== undefined && a[c[0]][c[1]] !== undefined) {
        a[c[0]][c[1]]++
        if (a[c[0]][c[1]] === 10) flashers.splice(0, 0, [c[0], c[1]])
      }
    }
  }
}

const increment = (a) => {
	for (let r = 0; r < a.length; r++) {
  	for (let c = 0; c < a[0].length; c++) {
    	a[r][c]++
      if (a[r][c] === 10) flashers.push([r, c])
    }
  }
}

const normalize = (a) => {
	let flashCount = 0
	for (let r = 0; r < a.length; r++) {
  	for (let c = 0; c < a[0].length; c++) {
    	if (a[r][c] > 9) {
      	a[r][c] = 0
        flashCount += 1
      }
    }
  }
  return flashCount === 100
}

const show = (a) => a.map(l => l.map(c => c === 0 ? '0' : ' ').join('')).join("\n")

const token = window.setInterval(() => {
	if (done) {
  	window.clearInterval(token)
    return
  }
  
  step += 1
  increment(a)
  flash(a)
  const allFlash = normalize(a)
  document.getElementById('grid').innerHTML = show(a)
  if (step === 100) {
    console.log(`FLASHES @ STEP 100 ${flashes}`)
  }
  if (allFlash) {
    done = true
    console.log(`ALL FLASH @ STEP ${step}`)
  }

}, 50)
