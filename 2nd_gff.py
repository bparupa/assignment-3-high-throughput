file_path = "C:\\Users\\bhava\\Downloads\\2088090036.gff"
genes=[]
with open(file_path,'r')as file:
    data = file.readlines()
    print(data)
    dummy =[]
    for line in data [1:]:
        parts = line.split()
        dummy.append(parts)
    final_list =[]
    for i in dummy:
        empty = []
        for j in range(len(i)):
            if j == 0 or j == 3 or j == 4 or j == 6:
                empty.append(i[j])
        final_list.append(empty)


data_now = []
for items in range(len(final_list)-1):
    gene_name =[]
    # gene_start = []
    # gene_end = []
    # gene_strand = []
    for loc in range(len(final_list[items])):
        if loc == 0:
            num = int(final_list[items + 1][1]) - int(final_list[items][2])
            # print(num)
            if num < 50 and num > -50:
                gene_name.append(final_list[items][0])
                # gene_start.append(final_list[items][0])
                # gene_end.append(final_list[items][1])
                # gene_strand.append(final_list[items][2])
                data_now.append(gene_name)
#                 # data_now.extend(gene_start)
#                 # data_now.extend(gene_end)
#                 # data_now.extend(gene_strand)
#                 # tmp.extend(final_list[items][0])
#                 # tmp.extend(final_list[items][1])
        
# # operons = []

# # for t in range(0,len(data_now),4):
# #     operons.append(data_now[t])