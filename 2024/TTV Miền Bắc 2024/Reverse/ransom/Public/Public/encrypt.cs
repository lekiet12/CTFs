using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;
public class Encyptor
{
	public static void Main()
	{
		byte[] bytes = Encoding.ASCII.GetBytes(Encyptor.s2);
		byte[] bytes2 = Encoding.ASCII.GetBytes(Encyptor.s);
		byte[] bytes3 = new PasswordDeriveBytes(Encyptor.strPassword, bytes2, Encyptor.strHashName, Encyptor.iterations).GetBytes(Encyptor.num / 8);
		Console.WriteLine("Key Bytes: " + BitConverter.ToString(bytes3));
	}
	private static string strPassword = "amp4Z0wpKzJ5Cg0GDT5sJD0sMw0IDAsaGQ1Afik6NwXr6rrSEQE=";
	private static string s = "aGQ1Afik6NampDT5sJEQE4Z0wpsMw0IDAD06rrSswXrKzJ5Cg0G=";
	private static string strHashName = "SHA1";
	private static int iterations = 2;
	private static int num = 256;
	private static string s2 = "@bbd1ec93108b0cb";
}

