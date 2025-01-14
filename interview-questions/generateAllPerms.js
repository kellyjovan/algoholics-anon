/**
given an array of strings, generate all unique permutations of each string
 */

function perms(...sArr) {
  const output = new Set();

  function helper(str, acc) {
    if (str.length === 0) return output.add(acc);
    for (let i = 0; i < str.length; i += 1) {
      const char = str[i];
      acc += char;
      helper(str.slice(0, i) + str.slice(i + 1), acc);
      acc = acc.slice(0, acc.length - 1);
    }
  }

  for (const s of sArr) {
    helper(s, '');
  }
  return [...output];
}

perms('sac', 'acs', 'cas', 'sas', 'hi');
