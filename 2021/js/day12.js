let m = {}
const a = [
  'fw-ll',
  'end-dy',
  'tx-fw',
  'tx-tr',
  'dy-jb',
  'ZD-dy',
  'dy-BL',
  'dy-tr',
  'dy-KX',
  'KX-start',
  'KX-tx',
  'fw-ZD',
  'tr-end',
  'fw-jb',
  'fw-yi',
  'ZD-nr',
  'start-fw',
  'tx-ll',
  'll-jb',
  'yi-jb',
  'yi-ll',
  'yi-start',
  'ZD-end',
  'ZD-jb',
  'tx-ZD'
]
  .forEach(line => {
  	const [a, b] = line.split('-')
    if (m[a] === undefined) m[a] = []
    if (m[b] === undefined) m[b] = []
    m[a].push(b)
    m[b].push(a)
  })

const findPaths = (visitTwice = false) => {
  let paths = 0
  var queue = [ 
    ['start', ['start'], false] 
  ]
  while (queue.length) {
    const [ cave, visitedCaves, secondVisit ] = queue.splice(0, 1)[0]
    if (cave === 'end') {
      paths++
      continue
    }
    m[cave].forEach(edge => {
      if (!visitedCaves.includes(edge)) {
        const newSmall = [ ...visitedCaves ]
        if (edge.toLowerCase() === edge) newSmall.push(edge)
        queue.push([edge, newSmall, secondVisit])
      } 
      else 
      if (visitTwice && 
      		visitedCaves.includes(edge) && 
          secondVisit === false && 
          !['start', 'end'].includes(edge)) {
        queue.push([edge, visitedCaves, true])
      }
    })
  }
	return paths
}

console.log(findPaths())
console.log(findPaths(true))