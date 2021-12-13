publicclass CxIntegrationTest

{

publicstatic void main (String [] args)

{

String accountNumber = args[1];

String query = "SELECT * FROM user_data WHERE acountNumber = " + accountNumber;



Statement statement = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);



ResultSet results = statement.executeQuery(query);

}
