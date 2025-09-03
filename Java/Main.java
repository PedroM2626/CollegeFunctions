package Java;

import java.util.Scanner;
import java.util.Random;

class Main {

    //Here is where the functions are declared
    public static void RockPaperScissors()
    {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();
        try {

            while (true)
            {
                System.out.print("Make your decision: 1 - rock, 2 - paper, 3 - scissors (0 to exit): ");
                int player = sc.nextInt();
                
                if (player == 0) {
                    System.out.println("Thanks for playing!");
                    break;
                }
                
                if (player < 1 || player > 3) {
                    System.out.println("Invalid choice! Try again.");
                    continue;
                }
                
                int AI = random.nextInt(3) + 1;

                if ((player == 1 && AI == 1) || (player == 2 && AI == 2) || (player == 3 && AI == 3))
                {
                    System.out.println("Draw!");
                }
                else if((player == 1 && AI == 3) || (player == 2 && AI == 1) || (player == 3 && AI == 2))
                {
                    System.out.println("Player wins!");
                }
                else
                {
                    System.out.println("AI wins!");
                }
            }
        } finally {
            sc.close();
        }
    }

    public static void GuessWord()
    {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();
        try {

            String[] words = {"password", "dog", "nephew", "java", "computer", "university"};
            String word = words[random.nextInt(words.length)];
            
            char[] message = new char[word.length()];
            
            for (int i = 0; i < word.length(); i++) {
                message[i] = '_';
            }
            
            int life = 5;
            boolean wordGuessed = false;

            while (life > 0 && !wordGuessed)
            {
                System.out.println("\nWord: " + String.valueOf(message));
                System.out.println("Lives left: " + life);
                System.out.print("Send a letter or guess the word: ");
                String input = sc.nextLine().toLowerCase();
                
                if (input.length() == 1) {
                    // Single letter guess
                    char letter = input.charAt(0);
                    boolean correctGuess = false;
                    
                    for (int i = 0; i < word.length(); i++) {
                        if (word.charAt(i) == letter) {
                            message[i] = letter;
                            correctGuess = true;
                        }
                    }
                    
                    if (correctGuess) {
                        System.out.println("Good guess!");
                    } else {
                        System.out.println("Wrong letter!");
                        life--;
                    }
                    
                    if (String.valueOf(message).equals(word)) {
                        wordGuessed = true;
                    }
                } else {
                    // Word guess
                    if (input.equals(word)) {
                        wordGuessed = true;
                    } else {
                        System.out.println("Wrong word!");
                        life--;
                    }
                }
            }
            
            if (wordGuessed) {
                System.out.println("Congratulations, you did it! The word was: " + word);
            } else {
                System.out.println("You lost! The word was: " + word);
            }
        } finally {
            sc.close();
        }
    }
    
    // This is the main function
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        try {
            while (true) {
                System.out.println("\n=== College Functions Games ===");
                System.out.println("1. Rock Paper Scissors");
                System.out.println("2. Guess the Word");
                System.out.println("0. Exit");
                System.out.print("Choose an option: ");
                
                int choice = sc.nextInt();
                sc.nextLine(); // Consume newline
                
                switch (choice) {
                    case 1:
                        RockPaperScissors();
                        break;
                    case 2:
                        GuessWord();
                        break;
                    case 0:
                        System.out.println("Thanks for playing!");
                        return;
                    default:
                        System.out.println("Invalid option!");
                }
            }
        } finally {
            sc.close();
        }
    }
}