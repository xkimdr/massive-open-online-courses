package dictionary;

import java.io.PrintWriter;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.Map;
import java.util.Scanner;

public class SaveableDictionary {
    private Map<String, String> dictionary;
    private String file;

    public SaveableDictionary() {
        this("");
    }

    public SaveableDictionary(String file) {
        this.dictionary = new HashMap<>();
        this.file = file;
    }

    public boolean load() {
        try (Scanner scan = new Scanner(Paths.get(this.file))) {
            while (scan.hasNextLine()) {
                String[] list = scan.nextLine().split(":");
                this.add(list[0], list[1]);
            }
            return true;
        } catch (Exception e) {
            System.out.println(e);
            return false;
        }
    }

    public void add(String words, String translation) {
        this.dictionary.putIfAbsent(words, translation);
        this.dictionary.putIfAbsent(translation, words);
    }

    public String translate(String word) {
        return this.dictionary.getOrDefault(word, null);
    }

    public void delete(String word) {
        this.dictionary.remove(this.dictionary.get(word));
        this.dictionary.remove(word);
    }

    public boolean save() {
        try (PrintWriter f = new PrintWriter(this.file)) {
            Set<String> s = new HashSet<>();
            for (String word : this.dictionary.keySet()) {
                if (s.contains(word)) {
                    continue;
                }
                String tl = this.dictionary.get(word);
                s.add(word);
                s.add(tl);
                f.println(word + ":" + tl);

            }
            return true;
        } catch (Exception e) {
            System.out.println(e);
            return false;
        }
    }
}
