def detect_contact(data, fluid_type):
    if fluid_type == ["gas", "oil", "water"]:
        X = data[['depth', 'temp', 'pressure']]
        y = data['fluid'].str.lower()
        model = nn(hidden_layer_sizes = (10,10,10), max_iter = 10000, random_state = 300)
        model.fit(X,y)
        predicted = model.predict(X)
        
        gas = X[['depth', 'pressure']][predicted == 'gas']
        oil = X[['depth', 'pressure']][predicted == 'oil']
        water = X[['depth', 'pressure']][predicted == 'water']

        reg_gas= LR()
        reg_oil= LR()
        reg_water= LR()

        reg_gas.fit(gas['depth'].values.reshape(-1,1),gas[ 'pressure'])
        reg_oil.fit(oil['depth'].values.reshape(-1,1),oil[ 'pressure'])
        reg_water.fit(water['depth'].values.reshape(-1,1),water[ 'pressure'])

        def line(p1, p2):
            A = (p1[1] - p2[1])
            B = (p2[0] - p1[0])
            C = (p1[0]*p2[1] - p2[0]*p1[1])
            return A, B, -C

        def intersection(L1, L2):
            D  = L1[0] * L2[1] - L1[1] * L2[0]
            Dx = L1[2] * L2[1] - L1[1] * L2[2]
            Dy = L1[0] * L2[2] - L1[2] * L2[0]
            if D != 0:
                x = Dx / D
                y = Dy / D
                return x,y
            else:
                return False

        x1 = np.array(0).reshape(1, -1)
        x2 = np.array(10000).reshape(1, -1)

        L1 = line([x1, reg_gas.predict(x1)], [x2, reg_gas.predict(x2)])
        L2 = line([x1, reg_oil.predict(x1)], [x2, reg_oil.predict(x2)])
        L3 = line([x1, reg_water.predict(x1)], [x2, reg_water.predict(x2)])

        print("GOC: ", intersection(L1, L2)[0][0][0])
        print("OWC: ", intersection(L2, L3)[0][0][0])
        
    elif fluid_type == [ "oil", "water"]:
        model = nn(hidden_layer_sizes = (10,10,10), max_iter = 10000, random_state = 300)
        model.fit(X,y)
        predicted = model.predict(X)
        
        oil = X[['depth', 'pressure']][predicted == 'oil']
        water = X[['depth', 'pressure']][predicted == 'water']

        reg_oil= LR()
        reg_water= LR()

        reg_oil.fit(oil['depth'].values.reshape(-1,1),oil[ 'pressure'])
        reg_water.fit(water['depth'].values.reshape(-1,1),water[ 'pressure'])

        def line(p1, p2):
            A = (p1[1] - p2[1])
            B = (p2[0] - p1[0])
            C = (p1[0]*p2[1] - p2[0]*p1[1])
            return A, B, -C

        def intersection(L1, L2):
            D  = L1[0] * L2[1] - L1[1] * L2[0]
            Dx = L1[2] * L2[1] - L1[1] * L2[2]
            Dy = L1[0] * L2[2] - L1[2] * L2[0]
            if D != 0:
                x = Dx / D
                y = Dy / D
                return x,y
            else:
                return False

        x1 = np.array(0).reshape(1, -1)
        x2 = np.array(10000).reshape(1, -1)

        L2 = line([x1, reg_oil.predict(x1)], [x2, reg_oil.predict(x2)])
        L3 = line([x1, reg_water.predict(x1)], [x2, reg_water.predict(x2)])

        print("OWC: ", intersection(L2, L3)[0][0][0])     
        
    else:
        model = nn(hidden_layer_sizes = (10,10,10), max_iter = 10000, random_state = 300)
        model.fit(X,y)
        predicted = model.predict(X)
        
        gas = X[['depth', 'pressure']][predicted == 'gas']
        water = X[['depth', 'pressure']][predicted == 'water']

        reg_gas= LR()
        reg_oil= LR()
        reg_water= LR()

        reg_gas.fit(gas['depth'].values.reshape(-1,1),gas[ 'pressure'])
        reg_water.fit(water['depth'].values.reshape(-1,1),water[ 'pressure'])

        def line(p1, p2):
            A = (p1[1] - p2[1])
            B = (p2[0] - p1[0])
            C = (p1[0]*p2[1] - p2[0]*p1[1])
            return A, B, -C

        def intersection(L1, L2):
            D  = L1[0] * L2[1] - L1[1] * L2[0]
            Dx = L1[2] * L2[1] - L1[1] * L2[2]
            Dy = L1[0] * L2[2] - L1[2] * L2[0]
            if D != 0:
                x = Dx / D
                y = Dy / D
                return x,y
            else:
                return False

        x1 = np.array(0).reshape(1, -1)
        x2 = np.array(10000).reshape(1, -1)

        L1 = line([x1, reg_gas.predict(x1)], [x2, reg_gas.predict(x2)])
        L3 = line([x1, reg_water.predict(x1)], [x2, reg_water.predict(x2)])

        print("GWC: ", intersection(L1, L3)[0][0][0])
        
