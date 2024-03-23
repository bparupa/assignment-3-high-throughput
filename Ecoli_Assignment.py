file_path = "C:\\Users\\bhava\\Downloads\\E_coli_K12_MG1655.ptt"
genes=[]
with open(file_path,'r')as file:
    data = file.readlines()
    for line in data [2:]:
        parts = line.split('..')
        
        for i in range(len(parts)):
            if i == 1:
                n = parts[i].split('\t')
                parts.extend(n)
        genes.append(parts)
        
        final_list = []
        for x in genes[1:]:
            tmp = []
            for j in range(len(x)):
                if j == 0 or j == 2 or j == 3 or j == 4 or j == 6:
                    tmp.append(x[j])
            final_list.append(tmp)
    # print(final_list)

data_now = []
for items in range(len(final_list)-1):
    gene_name =[]
    # gene_start = []
    # gene_end = []
    # gene_strand = []
    for loc in range(len(final_list[items])):
        if loc == 0:
            num = int(final_list[items + 1][0]) - int(final_list[items][1])
            if num < 50:
                gene_name.append(final_list[items][4])
                # gene_start.append(final_list[items][0])
                # gene_end.append(final_list[items][1])
                # gene_strand.append(final_list[items][2])
                data_now.append(gene_name)
                # data_now.extend(gene_start)
                # data_now.extend(gene_end)
                # data_now.extend(gene_strand)
                # tmp.extend(final_list[items][0])
                # tmp.extend(final_list[items][1])
        
# operons = []

# for t in range(0,len(data_now),4):
#     operons.append(data_now[t])