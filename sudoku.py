def sudoku():
    def reset():
        for i in range(0,rows,1):
            for j in range(0,cols,1):
                col[i][j].delete(0, "end")
                col[i][j].config(bg = 'lightgray')

    def check():
        incomplete = 0
        error = 0
        for i in range(0,rows):
            for j in range(0,cols):
                temp = col[i][j].get()
                if len(temp) > 1 or temp == '' or temp == ' ':
                    col[i][j].config(bg = 'Red')
                    incomplete = 1
                else:
                    col[i][j].config(bg = 'Lightgray')
        #row
        for i in range(0, rows):
            for j in range(0, cols):
                temp_p = col[i][j].get()
                if j == 0:
                    for k in [1, 2, 3, 4, 5, 6, 7, 8]:
                        temp_s = col[i][k].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[i][l].config(bg = 'yellow')
                            error = 1
                            break
                if j == 1:
                    for k in [0, 2, 3, 4, 5, 6, 7, 8]:
                        temp_s = col[i][k].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[i][l].config(bg = 'yellow')
                            error = 1
                            break
                if j == 2:
                    for k in [0, 1, 3, 4, 5, 6, 7, 8]:
                        temp_s = col[i][k].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[i][l].config(bg = 'yellow')
                            error = 1
                            break
                if j == 3:
                    for k in [0, 1, 2, 4, 5, 6, 7, 8]:
                        temp_s = col[i][k].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[i][l].config(bg = 'yellow')
                            error = 1
                            break
                if j == 4:
                    for k in [0, 1, 2, 3, 5, 6, 7, 8]:
                        temp_s = col[i][k].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[i][l].config(bg = 'yellow')
                            error = 1
                            break
                if j == 5:
                    for k in [0, 1, 2, 3, 4, 6, 7, 8]:
                        temp_s = col[i][k].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[i][l].config(bg = 'yellow')
                            error = 1
                            break
                if j == 6:
                    for k in [0, 1, 2, 3, 4, 5, 7, 8]:
                        temp_s = col[i][k].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[i][l].config(bg = 'yellow')
                            error = 1
                            break
                if j == 7:
                    for k in [0, 1, 2, 3, 4, 5, 6, 8]:
                        temp_s = col[i][k].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[i][l].config(bg = 'yellow')
                            error = 1
                            break
                if j == 8:
                    for k in [0, 1, 2, 3, 4, 5, 6, 7]:
                        temp_s = col[i][k].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[i][l].config(bg = 'yellow')
                            error = 1
                            break
        #column
        for j in range(0, rows):
            for i in range(0, cols):
                temp_p = col[i][j].get()
                if i == 0:
                    for k in [1, 2, 3, 4, 5, 6, 7, 8]:
                        temp_s = col[k][j].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[l][j].config(bg = 'yellow')
                            error = 1
                            break
                if i == 1:
                    for k in [0, 2, 3, 4, 5, 6, 7, 8]:
                        temp_s = col[k][j].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[l][j].config(bg = 'yellow')
                            error = 1
                            break
                if i == 2:
                    for k in [0, 1, 3, 4, 5, 6, 7, 8]:
                        temp_s = col[k][j].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[l][j].config(bg = 'yellow')
                            error = 1
                            break
                if i == 3:
                    for k in [0, 1, 2, 4, 5, 6, 7, 8]:
                        temp_s = col[k][j].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[l][j].config(bg = 'yellow')
                            error = 1
                            break
                if i == 4:
                    for k in [0, 1, 2, 3, 5, 6, 7, 8]:
                        temp_s = col[k][j].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[l][j].config(bg = 'yellow')
                            error = 1
                            break
                if i == 5:
                    for k in [0, 1, 2, 3, 4, 6, 7, 8]:
                        temp_s = col[k][j].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[l][j].config(bg = 'yellow')
                            error = 1
                            break
                if i == 6:
                    for k in [0, 1, 2, 3, 4, 5, 7, 8]:
                        temp_s = col[k][j].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[l][j].config(bg = 'yellow')
                            error = 1
                            break
                if i == 7:
                    for k in [0, 1, 2, 3, 4, 5, 6, 8]:
                        temp_s = col[k][j].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[l][j].config(bg = 'yellow')
                            error = 1
                            break
                if i == 8:
                    for k in [0, 1, 2, 3, 4, 5, 6, 7]:
                        temp_s = col[k][j].get()
                        if temp_p == temp_s and temp_p != '' and temp_s != '':
                            for l in range(0, cols):
                                col[l][j].config(bg = 'yellow')
                            error = 1
                            break
        #cube-1-rowise
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                temp_p = col[i][j].get()
                if j == 0:
                    for k in [0, 1, 2]:
                        for l in [1, 2]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 1:
                    for k in [0, 1, 2]:
                        for l in [0, 2]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 2:
                    for k in [0, 1, 2]:
                        for l in [0, 1]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-2-rowise
        for i in [0, 1, 2]:
            for j in [3, 4, 5]:
                temp_p = col[i][j].get()
                if j == 3:
                    for k in [0, 1, 2]:
                        for l in [4, 5]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 4:
                    for k in [0, 1, 2]:
                        for l in [3, 5]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 5:
                    for k in [0, 1, 2]:
                        for l in [3, 4]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-3-rowise
        for i in [0, 1, 2]:
            for j in [6, 7, 8]:
                temp_p = col[i][j].get()
                if j == 6:
                    for k in [0, 1, 2]:
                        for l in [7, 8]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 7:
                    for k in [0, 1, 2]:
                        for l in [6, 8]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 8:
                    for k in [0, 1, 2]:
                        for l in [6, 7]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-4-rowise
        for i in [3, 4, 5]:
            for j in [0, 1, 2]:
                temp_p = col[i][j].get()
                if j == 0:
                    for k in [3, 4, 5]:
                        for l in [1, 2]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 1:
                    for k in [3, 4, 5]:
                        for l in [0, 2]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 2:
                    for k in [3, 4, 5]:
                        for l in [0, 1]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-5-rowise
        for i in [3, 4, 5]:
            for j in [3, 4, 5]:
                temp_p = col[i][j].get()
                if j == 3:
                    for k in [3, 4, 5]:
                        for l in [4, 5]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 4:
                    for k in [3, 4, 5]:
                        for l in [3, 5]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 5:
                    for k in [3, 4, 5]:
                        for l in [3, 4]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-6-rowise
        for i in [3, 4, 5]:
            for j in [6, 7, 8]:
                temp_p = col[i][j].get()
                if j == 6:
                    for k in [3, 4, 5]:
                        for l in [7, 8]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 7:
                    for k in [3, 4, 5]:
                        for l in [6, 8]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 8:
                    for k in [3, 4, 5]:
                        for l in [6, 7]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-7-rowise
        for i in [6, 7, 8]:
            for j in [0, 1, 2]:
                temp_p = col[i][j].get()
                if j == 0:
                    for k in [6, 7, 8]:
                        for l in [1, 2]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 1:
                    for k in [6, 7, 8]:
                        for l in [0, 2]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 2:
                    for k in [6, 7, 8]:
                        for l in [0, 1]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-8-rowise
        for i in [6, 7, 8]:
            for j in [3, 4, 5]:
                temp_p = col[i][j].get()
                if j == 3:
                    for k in [6, 7, 8]:
                        for l in [4, 5]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 4:
                    for k in [6, 7, 8]:
                        for l in [3, 5]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 5:
                    for k in [6, 7, 8]:
                        for l in [3, 4]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-9-rowise
        for i in [6, 7, 8]:
            for j in [6, 7, 8]:
                temp_p = col[i][j].get()
                if j == 6:
                    for k in [6, 7, 8]:
                        for l in [7, 8]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 7:
                    for k in [6, 7, 8]:
                        for l in [6, 8]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if j == 8:
                    for k in [6, 7, 8]:
                        for l in [6, 7]:
                            temp_s = col[k][l].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-1-columnwise
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                temp_p = col[i][j].get()
                if i == 0:
                    for k in [0, 1, 2]:
                        for l in [1, 2]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 1:
                    for k in [0, 1, 2]:
                        for l in [0, 2]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 2:
                    for k in [0, 1, 2]:
                        for l in [0, 1]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-2-columnwise
        for i in [0, 1, 2]:
            for j in [3, 4, 5]:
                temp_p = col[i][j].get()
                if i == 3:
                    for k in [0, 1, 2]:
                        for l in [4, 5]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 4:
                    for k in [0, 1, 2]:
                        for l in [3, 5]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 5:
                    for k in [0, 1, 2]:
                        for l in [3, 4]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-3-columnwise
        for i in [0, 1, 2]:
            for j in [6, 7, 8]:
                temp_p = col[i][j].get()
                if i == 6:
                    for k in [0, 1, 2]:
                        for l in [7, 8]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 7:
                    for k in [0, 1, 2]:
                        for l in [6, 8]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 8:
                    for k in [0, 1, 2]:
                        for l in [6, 7]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [0, 1, 2]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-4-columnwise
        for i in [3, 4, 5]:
            for j in [0, 1, 2]:
                temp_p = col[i][j].get()
                if i == 0:
                    for k in [3, 4, 5]:
                        for l in [1, 2]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 1:
                    for k in [3, 4, 5]:
                        for l in [0, 2]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 2:
                    for k in [3, 4, 5]:
                        for l in [0, 1]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-5-columnwise
        for i in [3, 4, 5]:
            for j in [3, 4, 5]:
                temp_p = col[i][j].get()
                if i == 3:
                    for k in [3, 4, 5]:
                        for l in [4, 5]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 4:
                    for k in [3, 4, 5]:
                        for l in [3, 5]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 5:
                    for k in [3, 4, 5]:
                        for l in [3, 4]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-6-columnwise
        for i in [3, 4, 5]:
            for j in [6, 7, 8]:
                temp_p = col[i][j].get()
                if i == 6:
                    for k in [3, 4, 5]:
                        for l in [7, 8]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 7:
                    for k in [3, 4, 5]:
                        for l in [6, 8]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 8:
                    for k in [3, 4, 5]:
                        for l in [6, 7]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [3, 4, 5]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-7-columnwise
        for i in [6, 7, 8]:
            for j in [0, 1, 2]:
                temp_p = col[i][j].get()
                if i == 0:
                    for k in [6, 7, 8]:
                        for l in [1, 2]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 1:
                    for k in [6, 7, 8]:
                        for l in [0, 2]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 2:
                    for k in [6, 7, 8]:
                        for l in [0, 1]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [0, 1, 2]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-8-columnwise
        for i in [6, 7, 8]:
            for j in [3, 4, 5]:
                temp_p = col[i][j].get()
                if i == 3:
                    for k in [6, 7, 8]:
                        for l in [4, 5]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 4:
                    for k in [6, 7, 8]:
                        for l in [3, 5]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 5:
                    for k in [6, 7, 8]:
                        for l in [3, 4]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [3, 4, 5]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #cube-9-columnwise
        for i in [6, 7, 8]:
            for j in [6, 7, 8]:
                temp_p = col[i][j].get()
                if i == 6:
                    for k in [6, 7, 8]:
                        for l in [7, 8]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 7:
                    for k in [6, 7, 8]:
                        for l in [6, 8]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
                if i == 8:
                    for k in [6, 7, 8]:
                        for l in [6, 7]:
                            temp_s = col[l][k].get()
                            if temp_p == temp_s and temp_p != '' and temp_s != '':
                                for m in [6, 7, 8]:
                                    for n in [6, 7, 8]:
                                        col[m][n].config(bg = 'yellow')
                                error = 1
        #result
        if error == 1 and incomplete == 1:
            messagebox.showerror('Error', 'Incomplete with faults!')
        elif error == 1:
            messagebox.showerror('Error', 'Board is containing faults!')
        elif incomplete == 1:
            messagebox.showerror('Incomplete', 'Board is incomplete!')
        else:
            messagebox.showinfo('Congratulations', 'You won the game...')

    from tkinter import Tk, Canvas, Entry, Button, CENTER, IntVar, messagebox

    root = Tk()

    screen = Canvas(root, height = 430, width = 460)
    screen.pack()

    screen.create_text(215, 15, text = 'SUDOKU', font = 'calibri 20 bold')

    #vertical lines
    screen.create_line(127, 53, 127, 408)
    screen.create_line(232, 53, 232, 408)
    #horizontal lines
    screen.create_line(24, 170, 336, 170)
    screen.create_line(24, 290, 336, 290)

    x, y, n = 0, 0, 0

    cols, rows = 9, 9

    col = []

    for i in range(0,rows,1): 
        x = 0
        if i == 0:
            y += 70 
        else:
            y += 40
        rowc = []
        for j in range(0,cols,1):
            x += 40
            ent = Entry(root, width = 2, font = 'Calibri 20', bd = 0, justify = CENTER, bg = 'lightgray')
            screen.create_window(x, y, window = ent)
            rowc.append(ent)
            x -= 5
        col.append(rowc)

    check_button = Button(root, text = 'Check', font = 'Calibri 10 bold', bd = 0, bg = 'Green', fg = 'white', padx = 10, pady = 5, command = check)
    screen.create_window(400, 70, window = check_button)

    reset_button = Button(root, text = 'Reset', font = 'Calibri 10 bold', bd = 0, bg = 'Red', fg = 'white', padx = 10, pady = 5, command = reset)
    screen.create_window(400, 110, window = reset_button)


    root.mainloop()

