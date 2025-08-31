package Java;

class Main {

    //Here is where the functions are declared
    public static void RockPaperScissors()
    {
        Scanner sc = new Scanner(System.in);

        while (true)
        {
            System.out.print("Make your decision: 1 - rock, 2 - paper, 3 - scissors");
            int player = sc.nextInt();
            Random random = new Random();
            int AI = random.nextInt(3) + 1;

            if ((player == 1 && IA == 1) && (player == 2 && IA == 2) && (player == 3 && IA == 3))
            {
                System.out.println("Draw!");
            }
            else if((player == 1 && IA == 2) && (player == 3 && IA == 1) && (player == 2 && IA == 3))
            {
                System.out.println("AI wins!");
            }
            else if((player == 2 && IA == 1) && (player == 1 && IA == 3) && (player == 3 && IA == 2))
            {
                System.out.println("Player wins!");
            }
        }
    }

    public static void GuesWord()
    {
        Scanner sc = new Scanner(System.in);

        String[] words = ["password", "dog", "nephew"];
        Random random = new Random();
        int word = words.charAt(random.nextInt(3));

        String result  = "";
        String message = "";
        int life = 5;

        while (result == word && life > 0)
        {
            System.out.println("Send a letter(s), you have 5 lives: ");
            String pword = sc.nextLine();
            if (pword == word)
            {
                result += pword
            }
            for (int i == 0; i < word.Lenght; i++)
            {
                if(result.charAt(i) == word.charAt(i))
                {
                    message.charAt(i) = word.charAt(i);
                }
                else
                {
                    message.charAt(i) = "_";
                }
            }
            System.out.print(message);
            if (result == word)
            {
                System.out.println("Congratulations, you did it!");
            }

            life -= 1;
            if (life < 1)
            {
                System.out.println("You died, try again latter!");
            }
        }
    }
    
    // This is the main function
    public static void main(String[] args)
    {
        System.out.println("Hi");
    }
}