#include <stdio.h>
#include <ctype.h>
#include <math.h>

#define SIZE 1000

struct Card
{
    int number;
    int winningNumbers[SIZE];
    int winningNumbersCount;
    int numbers[SIZE];
    int numbersCount;
    int score;
    int matches;
    int clones;
};

char filePath[] = "../../input/day4";
struct Card cards[SIZE];
int cardsCount = 0;
int totalScore = 0;
int allCards = 0;

void readData();
void printCards();
int parseInt(char str[], int start, int size);
void bubbleSort(int array[], int size);

void calculateScore();

int main(int argc, char const *argv[])
{
    readData();
    calculateScore();
    // printCards();
    return 0;
}

void readData()
{
    FILE *input;
    input = fopen(filePath, "r");
    char line[SIZE];
    while (fgets(line, SIZE, input))
    {
        // start parsing after "Card"
        int i = 3;
        int cardIdStart = 4;
        int winningNumberStart = 0;
        int numbersStart = 0;

        while (1)
        {
            // search for :
            if (line[i] == ':')
            {
                winningNumberStart = i + 1;
                cards[cardsCount].number = parseInt(line, cardIdStart, i - cardIdStart);
            }

            if (line[i] == '|')
            {
                int winningNumbersCount = (i - winningNumberStart) / 3;
                cards[cardsCount].winningNumbersCount = winningNumbersCount;
                for (int j = 0; j < winningNumbersCount; j++)
                {
                    int num = parseInt(line, winningNumberStart + j * 3, 3);
                    cards[cardsCount].winningNumbers[j] = num;
                }
                bubbleSort(cards[cardsCount].winningNumbers, winningNumbersCount);
                numbersStart = i + 1;
            }

            if(line[i] == '\n')
            {
                int numbersCount = (i - numbersStart) / 3;
                cards[cardsCount].numbersCount = numbersCount;
                for (int j = 0; j < numbersCount; j++)
                {
                    int num = parseInt(line, numbersStart + j * 3, 3);
                    cards[cardsCount].numbers[j] = num;
                }
                bubbleSort(cards[cardsCount].numbers, numbersCount);
                // end of line, go to nex line
                break;
            }
            i++;
        }
        cardsCount++;
    }
    fclose(input);
}

void printCards()
{
    for (int i = 0; i < cardsCount; i++)
    {
        printf("Card number          : %3d\n", cards[i].number);
        printf("Winning numbers count: %3d\n", cards[i].winningNumbersCount);
        // printf("Winning numbers      :\n");
        // for (int j = 0; j < cards[i].winningNumbersCount; j++)
        // {
        //     printf("%3d", cards[i].winningNumbers[j]);
        // }
        // printf("\n");
        // printf("Numbers              :\n");
        // for (int j = 0; j < cards[i].numbersCount; j++)
        // {
        //     printf("%3d", cards[i].numbers[j]);
        // }
        // printf("\n");
        printf("Score                : %3d\n", cards[i].score);
        printf("Matches              : %3d\n", cards[i].matches);
        printf("Clones               : %3d\n", cards[i].clones);
        printf("\n");
    }
}

int parseInt(char str[], int start, int size)
{
    int num = 0;
    for (int i = start; i < start + size; i++)
    {
        if (str[i] == ' ')
        {
            continue;
        }
        if (!isdigit(str[i]))
        {
            return 0;
        }
        int multiplier = pow(10, start + size - i - 1);
        num += (str[i] - '0') * multiplier;
    }

    return num;
}

void bubbleSort(int array[], int size)
{
  // loop to access each array element
  for (int step = 0; step < size - 1; step++) {
      
    // loop to compare array elements
    for (int i = 0; i < size - step - 1; i++) {
      
      // compare two adjacent elements
      // change > to < to sort in descending order
      if (array[i] > array[i + 1]) {
        
        // swapping occurs if elements
        // are not in the intended order
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }
}

void calculateScore()
{
    for (int i = 0; i < cardsCount; i++)
    {
        for (int w = 0; w < cards[i].winningNumbersCount; w++)
        {
            for (int n = 0; n < cards[i].numbersCount; n++)
            {
                if (cards[i].winningNumbers[w] == cards[i].numbers[n])
                {
                    cards[i].matches++;
                    if (cards[i].score == 0)
                    {
                        cards[i].score = 1;
                    } 
                    else
                    {
                        cards[i].score *= 2;
                    }
                }
            }
        }
        // org card makes clones
        for (int c = i + 1; c <= i + cards[i].matches; c++)
        {
            cards[c].clones++;
        }
        // iterate over clones
        for (int copy = 0; copy < cards[i].clones; copy++)
        {
            for (int c = i + 1; c <= i + cards[i].matches; c++)
            {
                cards[c].clones++;
            }
        }
        allCards = allCards + 1 + cards[i].clones;
        totalScore += cards[i].score;
    }

    printf("Total score is: %d\n", totalScore);
    printf("All cards: %d\n", allCards);
}