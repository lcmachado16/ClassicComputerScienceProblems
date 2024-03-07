class CompressedGene:
    def __init__(self, gene:str) -> None:
        self._compress(gene)

    def _compress(self,gene:str) -> None:
        self.bit_string: int = 1 #começa com uma sentila 
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # desloca dois bits para a esquerda
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |=  0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalide Nucleotide:{}".format(nucleotide))
            
    def decompress(self) -> str:
        gene:str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:        #A
                gene += "A"
            elif bits == 0b01:      #C
                gene += "C"
            elif bits == 0b10:      #G 
                gene += "G"
            elif bits == 0b11:      #T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()
    

if __name__ == '__main__':
    from sys import getsizeof
    original: str = "TAGAAAGTA"
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original) #compacta 
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)
    print("Original and decompressed are the same: {}".format(original == compressed.decompress()))