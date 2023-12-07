#include <stdio.h>
#include <ctype.h>
#include <math.h>

FILE *input;
char fileName[] = "../../input/day3";
int cols = 0;
int rows = 0;

int foundNumbers = 0;
int foundGears = 0;

int sum = 0;

struct Number
{
    int row;
    int col;
    int length;
    int val;
};
struct Gear
{
    int row;
    int col;
};
char data[1000][1000];
struct Number numbers[1000*1000];
struct Gear gears[1000*1000];

void getSchematicSize();
void readData();
void findAllNumbers();
void printFoundNumbers();
int findAllGears();
void printFoundGears();
int getAdjacentNumber(int row, int col);
int hasAdjacentSymbol(int row, int col, int size);

int main(int argc, char const *argv[])
{
    
    getSchematicSize();
    readData();
    findAllNumbers();
    printFoundNumbers();

    for(int i = 0; i < foundNumbers; i++)
    {
        if(hasAdjacentSymbol(numbers[i].row, numbers[i].col, numbers[i].length))
        {
            sum+= numbers[i].val;
        }
    }

    printf("Result: %d\n", sum);

    printf("Gear: %d\n", findAllGears());
    // printFoundGears();
    return 0;
}

void getSchematicSize()
{
    input = fopen(fileName, "r");
    char c;
    while(1) {
        c = fgetc(input);
        if(c == EOF || c == '\n')
        {
            break;
        }
        cols+=1;
    }
    rows +=1;
    char line[1000];
    while(fgets(line, 1000, input))
    {
        rows +=1;
    }
    fclose(input);
    return;
}

void readData()
{
    input = fopen(fileName, "r");
    for(int i = 0; i < rows; i++)
    {
        fgets(data[i], cols+2, input);
    }
    fclose(input);
}

void findAllNumbers()
{
    for(int row = 0; row < rows; row++)
    {
        char currentNumber[100];
        int currentNumberStart = 0;
        int currentNumberEnd = 0;
        int processingNumber = 0;
        int position = 0;
        for(int col = 0; col < cols; col++)
        {
            if (isdigit(data[row][col]))
            {
                currentNumber[position] = data[row][col];
                if (processingNumber == 0)
                {
                    currentNumberStart = col;
                }
                processingNumber = 1;
                position++;

                if(col == cols - 1)
                {
                    int num = 0;
                    currentNumberEnd = col - 1;
                    for (int i = 0; i < position; i++) {
                        int multiplier = pow(10, position - i - 1);
                        num += (currentNumber[i] - '0') * multiplier;
                    }
                    numbers[foundNumbers].val = num;
                    numbers[foundNumbers].row = row;
                    numbers[foundNumbers].col = currentNumberStart;
                    numbers[foundNumbers].length = position;
                    position = 0;
                    processingNumber = 0;
                    foundNumbers++;
                }
            }
            else
            {
                if (processingNumber == 1)
                {
                    int num = 0;
                    currentNumberEnd = col - 1;
                    for (int i = 0; i < position; i++) {
                        int multiplier = pow(10, position - i - 1);
                        num += (currentNumber[i] - '0') * multiplier;
                    }
                    numbers[foundNumbers].val = num;
                    numbers[foundNumbers].row = row;
                    numbers[foundNumbers].col = currentNumberStart;
                    numbers[foundNumbers].length = position;
                    position = 0;
                    processingNumber = 0;
                    foundNumbers++;
                }

            }
        }
    }
}

void printFoundNumbers()
{
    for (int i = 0; i < foundNumbers; i++)
    {
        printf("number: %3d\n", numbers[i].val);
        printf("row   : %3d\n", numbers[i].row);
        printf("col   : %3d\n", numbers[i].col);
        printf("len   : %3d\n", numbers[i].length);
        printf("-----------\n");
    }
    
}

int findAllGears() {
    int sum = 0;
    for(int row = 0; row < rows; row++)
    {
        for(int col = 0; col < cols; col++)
        {
            if(data[row][col] == '*')
            {
                int gearRatio = getAdjacentNumber(row, col);
                if (gearRatio)
                {
                    gears[foundGears].row = row;
                    gears[foundGears].col = col;
                    foundGears++;
                    sum+=gearRatio;
                }
            }
        }
    }
    return sum;
}

int getAdjacentNumber(int row, int col)
{
    int found1 = -1;
    int found2 = -1;
    int adjacentNumber = 1;
    int foundCount = 0;
    for (int i = 0; i < foundNumbers; i++)
    {
        if (numbers[i].row <= row + 1 && numbers[i].row >= row - 1) {
            // check if last digit is adjacent
            int firstDigitCol = numbers[i].col;
            int lastDigitCol = numbers[i].col + numbers[i].length - 1;
            if (
                (lastDigitCol <= col + 1 && lastDigitCol >= col - 1) ||
                (firstDigitCol <= col + 1 && firstDigitCol >= col - 1)
            ) {
                printf("Numer %d in range left for row %d for col %d %d\n", numbers[i].val, row, numbers[i].col, col);
                foundCount++;
                adjacentNumber *= numbers[i].val;
            }
        }
    }
    if (foundCount == 2)
    {
        return adjacentNumber;
    }
    return 0;
}

void printFoundGears()
{
    for(int i = 0; i < foundGears; i++)
    {
        printf("Gear at row: %d, col: %d\n", gears[i].row, gears[i].col);
    }
    printf("Count: %d\n", foundGears);
}

int hasAdjacentSymbol(int row, int col, int size)
{
    int colStart = col - 1;
    int rowAbove = row - 1;
    for(int i = rowAbove; i < rowAbove + 3; i++) {
        if (i < 0 || i >= rows)
        {
            continue;
        }
        for(int j = colStart; j < colStart + size + 2; j ++)
        {
            if (j < 0 || j >= cols)
            {
                continue;
            }
            if (isdigit(data[i][j]) || data[i][j] == '.')
            {
                continue;
            }
            return 1;
        }
    }

    return 0;
}
