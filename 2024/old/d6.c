#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *filePtr = fopen("./data/day6.txt", "r");

    // Get file size 
    fseek(filePtr, 0, SEEK_END); 
    int size = ftell(filePtr); 
    fseek(filePtr, 0, SEEK_SET);

    // Read data
    char *rawData = (char*) calloc (size, sizeof(char));	
    fread(rawData, sizeof(char), size, filePtr);
    
    char *data[131];
    char *line;
    line = strtok(rawData,"\n");
    int ctr = 0;
    while(line != NULL)
    {
        data[ctr] = line;
        line = strtok(NULL,"\n");
        ctr++;
    }

    int rowIndex = -1;
    int colIndex = -1;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < strlen(data[i]); j++) {
            if (data[i][j] != '.' && data[i][j] != '#') {
                rowIndex = i;
                colIndex = j;
                break;
            }
        }
        if (colIndex != -1) {
            break;
        }
    }
    int startingRow = rowIndex;
    int startingCol = colIndex;

    // while (1) {
    //     int nextRowIndex = rowIndex;
    //     int nextColIndex = colIndex;
    //     switch (data[rowIndex][colIndex]) {
    //     case '^':
    //         nextRowIndex--;
    //         break;
    //     case '>':
    //         nextColIndex++;
    //         break;
    //     case 'v':
    //         nextRowIndex++;
    //         break;
    //     case '<':
    //         nextColIndex--;
    //         break;
    //     default:
    //         break;
    //     }

    //     if ((0 <= nextRowIndex && nextRowIndex < ctr && 0 <= nextColIndex && nextColIndex < strlen(data[rowIndex]))) {
    //         nextTile = data[nextRowIndex][nextColIndex];
    //     }
    //     switch (nextTile) {
    //     case '.':
    //         cursor = data[rowIndex][colIndex];
    //         distinctTiles++;
    //         data[rowIndex][colIndex] = 'X';
    //         if (!(0 <= nextRowIndex && nextRowIndex < ctr && 0 <= nextColIndex && nextColIndex < strlen(data[rowIndex]))) break;
    //         data[nextRowIndex][nextColIndex] = cursor;
    //         rowIndex = nextRowIndex;
    //         colIndex = nextColIndex;
    //         break;
    //     case 'X':
    //         cursor = data[rowIndex][colIndex];
    //         data[rowIndex][colIndex] = 'X';
    //         if (!(0 <= nextRowIndex && nextRowIndex < ctr && 0 <= nextColIndex && nextColIndex < strlen(data[rowIndex]))) break;
    //         data[nextRowIndex][nextColIndex] = cursor;
    //         rowIndex = nextRowIndex;
    //         colIndex = nextColIndex;
    //         break;
    //     case '#':
    //         direction = (direction + 1) % 4;
    //         data[rowIndex][colIndex] = directions[direction];
    //         break;
    //     default:
    //         break;
    //     }
    //     if (!(0 <= nextRowIndex && nextRowIndex < ctr && 0 <= nextColIndex && nextColIndex < strlen(data[rowIndex]))) break;
    // }
    // printf("Distinct tiles: %d\n", distinctTiles);
    // for (int i = 0; i < ctr; i++) {
    //     printf("%s\n", data[i]);
    // }
    int direction = 0;
    int distinctTiles = 0;
    char nextTile;
    char cursor;
    char cursorMask = 240;
    char visitedMask = 15;
    char directions[4] = { 16, 32, 64, 128 };
    char visitedDirection[4] = { 1, 2, 4, 8 };
    while (1) {
        int nextRowIndex = rowIndex;
        int nextColIndex = colIndex;
        char currentTile = data[rowIndex][colIndex] & cursorMask;
        switch (currentTile) {
        case 16:
            nextRowIndex--;
            break;
        case 32:
            nextColIndex++;
            break;
        case 64:
            nextRowIndex++;
            break;
        case 128:
            nextColIndex--;
            break;
        default:
            break;
        }

        if ((0 <= nextRowIndex && nextRowIndex < ctr && 0 <= nextColIndex && nextColIndex < strlen(data[rowIndex]))) {
            nextTile = data[nextRowIndex][nextColIndex] & visitedDirection;
        }
        switch (nextTile) {
        case '.':
            data[rowIndex][colIndex] = directionsMap[direction];
            if (!(0 <= nextRowIndex && nextRowIndex < ctr && 0 <= nextColIndex && nextColIndex < strlen(data[rowIndex]))) break;
            data[nextRowIndex][nextColIndex] = currentTile | ;
            rowIndex = nextRowIndex;
            colIndex = nextColIndex;
            break;
        case '#':
            direction = (direction + 1) % 4;
            data[rowIndex][colIndex] = directions[direction];
            break;
        default:
            cursor = data[rowIndex][colIndex];
            data[rowIndex][colIndex] |= directionsMap[direction];
            if (!(0 <= nextRowIndex && nextRowIndex < ctr && 0 <= nextColIndex && nextColIndex < strlen(data[rowIndex]))) break;
            data[nextRowIndex][nextColIndex] = cursor;
            rowIndex = nextRowIndex;
            colIndex = nextColIndex;
            break;
        }
        if (!(0 <= nextRowIndex && nextRowIndex < ctr && 0 <= nextColIndex && nextColIndex < strlen(data[rowIndex]))) break;
    }

    fclose(filePtr);
    return 0;
}