
const upsert = (m, k, v) => {
	if (m[k] === undefined) m[k] = 0
  m[k] += v
  return m
}

const runRules = (p, r) => {
	let m = {}
  Object.keys(p).forEach((k) => {
    m = upsert(m, k[0] + r[k], p[k])
    m = upsert(m, r[k] + k[1], p[k])
  })
  return m
}

const map = (p, s) => {
	let m = {}
  Object.keys(p).forEach((k) => {
  	m = upsert(m, k[0], p[k])
  })
  m[s.substring(s.length - 1)] += 1
  var v = Object.values(m)  
  return {
  	map: m,
    max: Math.max(...v),
    min: Math.min(...v)
  }
}

let rules = {
  'NS': 'P',
  'KV': 'B',
  'FV': 'S',
  'BB': 'V',
  'CF': 'O',
  'CK': 'N',
  'BC': 'B',
  'PV': 'N',
  'KO': 'C',
  'CO': 'O',
  'HP': 'P',
  'HO': 'P',
  'OV': 'O',
  'VO': 'C',
  'SP': 'P',
  'BV': 'H',
  'CB': 'F',
  'SF': 'H',
  'ON': 'O',
  'KK': 'V',
  'HC': 'N',
  'FH': 'P',
  'OO': 'P',
  'VC': 'F',
  'VP': 'N',
  'FO': 'F',
  'CP': 'C',
  'SV': 'S',
  'PF': 'O',
  'OF': 'H',
  'BN': 'V',
  'SC': 'V',
  'SB': 'O',
  'NC': 'P',
  'CN': 'K',
  'BP': 'O',
  'PC': 'H',
  'PS': 'C',
  'NB': 'K',
  'VB': 'P',
  'HS': 'V',
  'BO': 'K',
  'NV': 'B',
  'PK': 'K',
  'SN': 'H',
  'OB': 'C',
  'BK': 'S',
  'KH': 'P',
  'BS': 'S',
  'HV': 'O',
  'FN': 'F',
  'FS': 'N',
  'FP': 'F',
  'PO': 'B',
  'NP': 'O',
  'FF': 'H',
  'PN': 'K',
  'HF': 'H',
  'VK': 'K',
  'NF': 'K',
  'PP': 'H',
  'PH': 'B',
  'SK': 'P',
  'HN': 'B',
  'VS': 'V',
  'VN': 'N',
  'KB': 'O',
  'KC': 'O',
  'KP': 'C',
  'OS': 'O',
  'SO': 'O',
  'VH': 'C',
  'OK': 'B',
  'HH': 'B',
  'OC': 'P',
  'CV': 'N',
  'SH': 'O',
  'HK': 'N',
  'NO': 'F',
  'VF': 'S',
  'NN': 'O',
  'FK': 'V',
  'HB': 'O',
  'SS': 'O',
  'FB': 'B',
  'KS': 'O',
  'CC': 'S',
  'KF': 'V',
  'VV': 'S',
  'OP': 'H',
  'KN': 'F',
  'CS': 'H',
  'CH': 'P',
  'BF': 'F',
  'NH': 'O',
  'NK': 'C',
  'OH': 'C',
  'BH': 'O',
  'FC': 'V',
  'PB': 'B'
}
let p = 'CKFFSCFSCBCKBPBCSPKP'

let pairs = {}
for (let i = 0; i < p.length - 1; i++) {
	upsert(pairs, p[i] + p[i+1], 1)
}
for (let i = 1; i <= 40; i++) {
	pairs = runRules(pairs, rules)
  if (i === 10) {
    const m = map(pairs, p)
    console.log(`@ 10 = ${m.max - m.min}`)
  }
  if (i === 40) {
    const m = map(pairs, p)
    console.log(`@ 40 = ${m.max - m.min}`)
  }
}