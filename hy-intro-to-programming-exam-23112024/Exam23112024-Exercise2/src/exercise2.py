# Write your solution to exercise 2 here


def find_gene_positions(gene: str, genome: str):
    result = []
    start_index = 0
    lg = len(gene)
    while True:
        index = genome.find(gene, start_index)
        if index == -1:
            break
        result.append(index)
        start_index = index + lg

    if len(result) == 0:
        return None
    return result


if __name__ == "__main__":
    genome = "ATCGAGATCGACGATCGTAGCTAGCTAGCTAGCGATCGA"
    gene1 = "TAGCTA"
    gene2 = "ATCGA"
    gene3 = "X"

    print(find_gene_positions(gene1, genome))
    print(find_gene_positions(gene2, genome))
    print(find_gene_positions(gene3, genome))
    print(type((find_gene_positions(gene3, genome))))
