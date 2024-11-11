public class Statistics {
    private String homeTeamName;
    private String visitingTeamName;
    private int homeTeamPoints;
    private int visitingTeamPoints;

    public Statistics(String homeTeamName, String visitingTeamName, int homeTeamPoints, int visitingTeamPoints) {
        this.homeTeamName = homeTeamName;
        this.visitingTeamName = visitingTeamName;
        this.homeTeamPoints = homeTeamPoints;
        this.visitingTeamPoints = visitingTeamPoints;
    }

    public String getHomeTeamName() {
        return this.homeTeamName;
    }

    public String getVisitingTeamName() {
        return this.visitingTeamName;
    }

    public int getHomeTeamPoints() {
        return this.homeTeamPoints;
    }

    public int getVisitingTeamPoints() {
        return this.visitingTeamPoints;
    }
}
