# Elevation Network Geodesy (1D)

A script for solving elevation networks in geodesy with Least Squares Method, but not for profesional use as it may contain bugs<br/>
Input --> Ortho Heights in .txt<br/>
Output --> Corrected Ortho Heights in .txt and info about the Network Quality

---

# Features

- Solves every 1 Dimentional Elevation Netowrk wthich consists of Ortho Heights
- Outputs a .txt with the Corrected Ortho Heights
- Generates A PDF file with the report of the Network Quality which contains every points height with its error (from covariance matrix), Sigma 0 value and Residuals of every height


# Input Data

Input Data should be ortho height of the points, and its distances between points. See demo_data.txt for reference. Every input data should look like this

r8-r9 2.534 <br/>
r8-r14 5.722 <br/>
r7-r9 1.416 <br/>
r7-r14 4.649 <br/>
r9-r10 1.567 <br/>
r9-r11 2.647 <br/>
r9-r12 5.573 <br/>
r9-r14 3.188 <br/>

**Static Point** is defined inside the code in line 167 and 168, its defined by tha value and name</br >
After height value, data can be blank like above or set a value for distance between 2 points

---

# Greek - Υψομετρικο Δικτυο
Το παραπάνω πρόγραμμα έχει γραφτεί σε Python 3.9 και μπορεί να χρησιμοποιηθεί για την συνόρθωση ενός υψομετρικού δικτιού. Δεν είναι για επαγγελματική χρήση καθώς μπορεί να περιέχει bugs τα οποία δεν έχουν ακόμα λυθεί.
Τα δεδομένα πρέπει να είναι σε αρχείο .txt με την μορφή όπως φαίνεται στο αρχείο demo_data.txt οπως το παραδειγμα απο κατω (ονοματα σημειων, υψομετρικη διαφορα, αποσταη μεταξυ σημειων--> αυτο μπορει να παραλειφθει)</br>
</br >π.χ r1-r2 2.938 1.2 </br >
</br >Το πρόγραμμα λειτουργεί με μονάδες μετρήσεις τα μετρά. Το πρόγραμμα κάνει την συνόρθωση με την μέθοδο των ελάχιστων εξωτερικών δεσμεύσεων και για αυτό το λόγο μέσα στο πρόγραμμα πρέπει να δηλωθεί πιο σημείο είναι το σταθερό και το υψόμετρο του όπως και την τοποθεσία του αρχείου που είναι τα δεδομένα. H αβεβαιότητά μεταξύ των μετρήσεων ειναι βάση απόστασης μεταξύ κορυφών το οποίο πρέπει να δηλωθεί στα δεδομένα μετά το υψόμετρο σε km. Το πρόγραμμα από default θα έχει πίνακα βαρών (P) μοναδιαίο το οποιο μπορει να αλλαξει απο το org_data βαζοντας να περνει τιμες το s_dist.</br >
</br >Τελικα το προγραμμα επιστρεφει ενα αρχειο output.txt με μονο τα υψομετρα μεσα, ενα αρχειο report.txt με διαφορα δεδομενα της συνορθωσης και τελικα ενα .pdf αρχειο οπου εχει μεσα αναλυτικα πληροφοριες για την συνορθωση οπως το σο οπου εχει μοναδες μετρα και τα υπολοιπα του πινακα δλ για την ερευση καποιου προβληματικου δεδομενου.</br >
</br >Απαραιτητα Libraries ειναι τα NumPy και FPDF



