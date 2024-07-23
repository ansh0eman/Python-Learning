def identifyTheColorSheets(n,m, paintingSheet, shotCoordinates):

    sheet_color = [0] * n 
    
    for shot in shotCoordinates:
        x,y, color = shot
        for sheet in range(n):
            x1,y1,x2,y2 = paintingSheet[sheet]
            if(x1<= x <=x2 and y1<= y <= y2):
                sheet_color[sheet] += 1
    for i in range(n):
        print(sheet_color[i])



def main():
    n,m = map(int, input().split())
    paintingSheet = []
    for i in range(n):
        row = list(map(int,input().split()))
        paintingSheet.append(row)
    shotCoordinates = []
    for i in range(m):
        row = list(map(int, input().split()))
        shotCoordinates.append(row)

    identifyTheColorSheets(n,m, paintingSheet, shotCoordinates)

main()