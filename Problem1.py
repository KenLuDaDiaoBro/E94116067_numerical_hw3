P_X = [0.698 , 0.733 , 0.768 , 0.803 , 0.838]
P_Y = [0.7661 , 0.7432 , 0.7193 , 0.6946 , 0.6690]
P_ACCX = 0.750
P_ACCY = 0.7317

for order in range(1 , 5):
    F = 0
    for i in range(0 , order):
        L = 1
        for j in range(0 , order):  
            if(i != j):
                L = L * (P_ACCX - P_X[j]) / (P_X[i] - P_X[j])
        F = F + P_Y[i] * L
    F = round(F , 8)
    Error = round(abs(F - P_ACCY) , 8)
    print(f"Order {order}: {F} , Error: {Error:.8f}")
