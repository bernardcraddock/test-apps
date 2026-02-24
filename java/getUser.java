public User getUser(int id) {
    Connection conn = DriverManager.getConnection(url, user, pass);
    Statement stmt = conn.createStatement();
    ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE id = " + id);
    if (rs.next()) {
        return new User(rs.getInt("id"), rs.getString("name"));
    }
    return null;
}
