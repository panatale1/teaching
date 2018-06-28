import java.util.Scanner;

public class assignment4{
	public static void main(String[] args){
		System.out.println("Guess a number!");
		System.out.println("Your number is: " + guess(1, 1000000));
	}
	public static int guess(int low, int high){
		if (low==high) return low;
		int mid = (high + low)/2;
		Scanner kb = new Scanner(System.in);
		System.out.println("Is your number " + mid + "?(yes/no)");
		String response = kb.nextLine();
		if (response.equalsIgnoreCase("yes") || response.equalsIgnoreCase("y")) return mid;
		System.out.println("Is your number larger than " + mid + "?(yes/no)");
		response = kb.nextLine();
		if (response.equalsIgnoreCase("yes") || response.equalsIgnoreCase("y")) return guess(mid+1, high);
		else return guess(low, mid-1);
	}
}
