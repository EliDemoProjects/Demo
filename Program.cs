using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;

namespace SQLi_1
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                var user = args[0];
                var pwd = Encrypt(args[1]);
                Login(user, pwd);
                var password = "1!.Acjjjj";
                var password2 = "1!.Acjjjj";
            }
            catch
            {
                Console.WriteLine("An error has occurred !!");
            }
        }

        private static string Encrypt(string plain)
        {
            return plain;
        }

        private static void Login(string username, string password)
        {
            try
            {
                string connectionString = "Server=myServer;Database=myDB;User Id=admin;Password=1!.Acjjjj;";

                using (SqlConnection conn = new SqlConnection(connectionString))
                {
                    conn.Open();

                    // Vulnerable to SQL injection — string concatenation
                    string query = "SELECT * FROM Users WHERE Username = '" + username + "' AND Password = '" + password + "'";

                    SqlCommand cmd = new SqlCommand(query, conn);
                    SqlDataReader reader = cmd.ExecuteReader();

                    if (reader.HasRows)
                    {
                        Console.WriteLine("Login successful.");
                        while (reader.Read())
                        {
                            Console.WriteLine("User: " + reader["Username"]);
                        }
                    }
                    else
                    {
                        Console.WriteLine("Invalid credentials.");
                    }
                }
            }
            catch
            {
                Console.WriteLine("An error has occurred !!");
            }
        }
    }
}
