let TrieNode = function () {
  this.children = {};
  this.isEndOfWord = false;
};

let Trie = function () {
  this.root = new TrieNode();
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
  let node = this.root;
  for (let i = 0; i < word.length; i++) {
    const char = word[i];
    // 노드를 만들어 연속적으로 트리 형태로 만들어줌
    if (!(char in node.children)) {
      node.children[char] = new TrieNode();
    }
    node = node.children[char];
  }
  // 글자 연결을 마쳤다면 단어 끝의 마지막 char 여부를 저장하고 종료
  node.isEndOfWord = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
  let node = this.root;
  for (let i = 0; i < word.length; i++) {
    const char = word[i];
    if (!(char in node.children)) {
      return false; // 이어지지 않으면 찾지 못함
    }
    node = node.children[char];
  }
  return node.isEndOfWord; // 마지막 단어여야 완전한 한 단어이기 때문
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
  let node = this.root;
  for (let i = 0; i < prefix.length; i++) {
    const char = prefix[i];
    if (!(char in node.children)) {
      return false; // 이어지지 않으면 찾지 못함
    }
    node = node.children[char];
  }
  return true; // search 문과 달리 prefix 만 일치하면 되기 때문에
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */

// 후기

// 문제 이해하기
// 해당 문제는 트리 구조를 활용하여 문자열 데이터의 character을 키로 저장하고 효율적으로 검색할 수 있도록 구현하는 문제이다.
// 추가로, 샘플코드가 class 형태로 제공이 되기 때문에 이에 대한 이해도가 필요할 것 같다.
// 만약 'apple' 과 'app' 이라는 문자열이 insert 문으로 주어진다면 아래 같은 트리 구조로 만들어지는 것이다.
//   'a'
// 'p' 'p'
// 'p' 'p'
// 'l'
// 'e'

// 해결 방안
// search, startsWith 함수의 차이는 완전한 단어인지, prefix 로 포함되는지 를 따지는 것이다.
// 따라서 각 노드마다 하나의 character 을 저장하고, 마지막 char인지 유무를 나타내는 Boolean 값도 활용할 것이다.

// 결론
// 구조 설계를 잘 할 수 있는지 파악하는 문제로 인식했다!
