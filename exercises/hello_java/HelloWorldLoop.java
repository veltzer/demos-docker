class HelloWorld
{
	public static void main(String args[])
	{
		while(true) {
			System.out.println("Hello from Java inside a Docker image");
			try
			{
				    Thread.sleep(1000);
			}
			catch(InterruptedException ex)
			{
				    Thread.currentThread().interrupt();
			}
		}
	}
}
