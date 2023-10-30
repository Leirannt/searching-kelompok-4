import random
import math

# Fungsi Matematis Pada Soal
def function(x1, x2):
    return - (math.sin(x1) * math.cos(x2) + 4/5 * math.exp(1 - math.sqrt(x1**2 + x2**2)))

# Inisialisasi populasi awal
def InisialisasiPopulasi(populasi, size):

    # Mengisi populasi dengan kromosom dengan representasi Real
    for _ in range(size):
        x1 = random.uniform(0, 1)
        x2 = random.uniform(0, 1)
        x3 = random.uniform(0, 1)
        x4 = random.uniform(0, 1)
        x5 = random.uniform(0, 1)
        x6 = random.uniform(0, 1)
        populasi.append([x1, x2, x3, x4, x5, x6])
    return populasi

# Dekode kromosom (x = rb + ((ra - rb)/N))
def decode(kromosom):
    x = kromosom
    x1 = -10 + ((10 - (-10))/3)*(x[0] + x[1] + x[2])
    x2 = -10 + ((10 - (-10))/3)*(x[3] + x[4] + x[5])
    return x1, x2

# Perhitungan fitness
def fitness(kromosom):
    x1, x2 = decode(kromosom)
    f = 1/function(x1, x2)+0.01
    return f

# seleksi parent (tournamen selection)
def selectParent(populasi, size, tournament_size):
    parents = []
    for _ in range(size // 2):
        # Memilih secara acak sejumlah kromosom untuk turnamen
        tournament = random.sample(populasi, tournament_size)

        # Menentukan pemenang turnamen (kromosom dengan fitness tertinggi)
        winner = max(tournament, key=fitness)
        
        parents.append(winner)
    
    return parents
    
# Crossover dengan metode Whole Arithmetic Crossover (dengan probabilitas 0.8)
def crossover(parent1, parent2):
    if random.random() < 0.8:
        i = 0
        p1 = []
        p2 = []
        for _ in range(6):
            p1.append(0.5*parent1[i] + (1-0.5)*parent2[i])
            p2.append(0.5*parent1[i] + (1-0.5)*parent2[i])
            i = i + 1
        child1 = p1
        child2 = p2
    else:
        child1 = parent1
        child2 = parent2
    
    return child1, child2

# Mutasi dengan metode Uniform Mutation (dengan probabilitas 0.05)
def mutation(child1, child2):
    if random.random() < 0.05: # Mutasi child dari parent 1
        i = random.randint(0, 5)
        child1[i] = random.uniform(0, 1)

    if random.random() < 0.05: # Mutasi child dari parent 2
       i = random.randint(0, 5)
       child2[i] = random.uniform(0, 1)
    
    return child1, child2

# Inisialisasi populasi
p = []
populasi = InisialisasiPopulasi(p, 100) # Jumlah populasi = 100

# Kriteria penghentian evolusi (loop) 
jumlah_generasi = 100

# Probabilitas operasi genetik (𝑃𝑐 dan 𝑃𝑚 )
crossover_prob = 0.8
mutation_prob = 0.05


# Seleksi survivor dengan Generational Model
for gen in range(jumlah_generasi):

    # Seleksi orangtua menggunakan roulette wheel (Fitness proportionate selection)
    parents = []
    for x in range(len(populasi)//2):

        tournament_size = 2  # Anda dapat menyesuaikan ukuran turnamen sesuai kebutuhan
    parent1 = random.choice(selectParent(populasi, len(populasi), tournament_size))
    parent2 = random.choice(selectParent(populasi, len(populasi), tournament_size))
    parents.append((parent1, parent2))
        
    new_population = []

    for parent1, parent2 in parents:
        # Crossover dengan metode Whole Arithmetic Crossover (dengan probabilitas 0.8)

        child1, child2 = crossover(parent1, parent2)

        # Mutasi dengan metode Uniform Mutation (dengan probabilitas 0.05)
        
        child1M, child2M = mutation(child1, child2)

    # Memasukkan child ke populasi generasi baru
        new_population.append(child1M)
        new_population.append(child2M)

    populasi = new_population

# Hasil Akhir (Output)
populasi_hasil_akhir_decoded = []
for x in populasi:
    k = decode(x)
    populasi_hasil_akhir_decoded.append(k)

hasil = []
for x in populasi_hasil_akhir_decoded:
    hasil.append(function(x[0], x[1]))

best = min(hasil)

for x in populasi_hasil_akhir_decoded:
    if (function(x[0], x[1]) == best):
        best_k = x

print('Kromosom Terbaik : ', best_k)
print('X1 = ', best_k[0])
print('X2 = ', best_k[1])
print('Nilai Minimum dari Fungsi : ', best)

