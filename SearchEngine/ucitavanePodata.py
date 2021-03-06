import os
import time

from parserTrie.Tree import *
from parserTrie.Parser import Parser
from parserTrie.Tree import TreeNode
from parserGraph.Parser import Parser
from parserGraph.Graph import *
#from .set import Set
from set import *
def popunjavanjeStruktura(path):
    trie = Tree()
    parser = Parser()
    directed = True
    g = Graph(directed)
    parser = Parser()

    start = time.time()
    trie.root = TreeNode('*')
    E = []
    link = ''
    recnikStranicaReci = dict()
    setSvihDatoteka = Set('')
    for root, dirs, files in os.walk(path, topdown=False):
        for filename in files:
            if r".html" in filename:
                absPath = os.path.join(root, filename)
                setSvihDatoteka.elements.append(absPath)
                parser.parse(os.path.join(root, filename))
                for word in parser.words:
                    add(trie.root, word.lower(),absPath)

                for links in parser.links:
                    for c in range(len(links)-1,0,-1):

                        if links[c] == "\\" or "/":

                            link = links
                            E.append([absPath, link, links])
                            break
                recnikStranicaReci[absPath] = parser.words
                #print ("dict['Name']: ", recnikStranicaReci[absPath])
                #print("\n\n")




    g,dokumentiKojiImajuLinkKaDokumentu,bekLinkovi = add_elements_to_Graph(E, directed)
    end = time.time()
    #print("Parsed files and loaded the Trie and Graph structure in " + str((end - start).__round__(2)) + " seconds.")
    return trie,g,setSvihDatoteka, recnikStranicaReci, dokumentiKojiImajuLinkKaDokumentu,bekLinkovi