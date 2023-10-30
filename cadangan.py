# def selectParent(populasi, size):
#     total_fitness = 0

#     for i in populasi:
#         total_fitness = fitness(i)
    
#     r = random.random()
#     i = 0

#     while(r>0):
#         r = r - (fitness(populasi[i])/total_fitness)
#         i = i + 1
#         if (i == (len(populasi)-1)):
#             break
#     parent = populasi[i]
#     return parent