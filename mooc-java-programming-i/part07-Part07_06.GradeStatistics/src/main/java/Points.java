public class Points {
    private int participants;
    private int passingParticipants;
    private int sum;
    private int passingSum;
    private int[] gradesDistribution;

    public Points() {
        this.participants = 0;
        this.passingParticipants = 0;
        this.sum = 0;
        this.passingSum = 0;
        this.gradesDistribution = new int[6];
    }

    public void add(int num) {
        if (num < 0 || num > 100) {
            return;
        }

        ++this.participants;
        this.sum += num;

        if (num >= 50) {
            ++this.passingParticipants;
            this.passingSum += num;
        }

        if (num >= 90) {
            ++this.gradesDistribution[5];
        } else if (num >= 80) {
            ++this.gradesDistribution[4];
        } else if (num >= 70) {
            ++this.gradesDistribution[3];
        } else if (num >= 60) {
            ++this.gradesDistribution[2];
        } else if (num >= 50) {
            ++this.gradesDistribution[1];
        } else {
            ++this.gradesDistribution[0];
        }
    }

    private double average() {
        if (this.participants == 0) {
            return -1;
        }

        return (double) this.sum / this.participants;
    }

    private double passingAverage() {
        if (this.passingParticipants == 0) {
            return -1;
        }

        return (double) this.passingSum / this.passingParticipants;
    }

    private double passingPercentage() {
        if (this.participants == 0) {
            return -1;
        }

        return 100.0 * this.passingParticipants / this.participants;
    }

    public void printAverage() {
        double avg = this.average();

        if (avg == -1) {
            System.out.println("Point average (all): -");
        } else {
            System.out.println("Point average (all): " + avg);
        }
    }

    public void printPassingAverage() {
        double avg = this.passingAverage();

        if (avg == -1) {
            System.out.println("Point average (passing): -");
        } else {
            System.out.println("Point average (passing): " + avg);
        }
    }

    public void printPassingPercentage() {
        double per = this.passingPercentage();

        if (per == -1) {
            System.out.println("Pass percentage: 0.0");
        } else {
            System.out.println("Pass percentage: " + per);
        }
    }

    private String star(int num) {
        String s = "";

        for (int i = 0; i < num; ++i) {
            s += "*";
        }

        return s;
    }

    public void printGradeDistribution() {
        System.out.println("Grade distribution:");

        for (int i = 5; i != -1; --i) {
            System.out.println(i + ": " + this.star(this.gradesDistribution[i]));
        }
    }
}
