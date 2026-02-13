# LeetCode No.208 实现 Trie (前缀树)

## 题目链接: https://leetcode.cn/problems/implement-trie-prefix-tree/description/

## 题目描述
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 
## 解题思路
- ** 方法 1 ** ：定义一个Trienode类来表示Trie树的节点，
每个节点包含一个字典来存储子节点和一个布尔值来标记是否是一个完整的单词。Trie类包含插入、搜索和前缀搜索的方法。插入方法将单词逐字符插入Trie树中，搜索方法检查单词是否存在于Trie树中，前缀搜索方法检查是否存在以给定前缀开头的单词。


📌 [查看 Python 代码](../solutions/python/No_208_实现Trie.py)