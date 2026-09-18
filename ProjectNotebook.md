Data Flow Diagram:

User types command: python3 main.py books/frankenstein.txt
                      │
                      ▼
                    main.py
 • Grabs the book file name that the user typed in
                      │
         ┌────────────┴────────────┐
         │ (If the file name is    │ (If the file name
         │  wrong)                 │  works)
         ▼                         ▼
   Prints an error message   Opens the book and reads
   & shuts down safely       all the text inside
                                   │
                                   ▼ 
                                   (Sends the text)
                             stats.py -> get_num_words
                              • Chops text into words
                                   │
                                   ▼ 
                                 (Sends the word total)
                             stats.py -> get_chars_dict
                              • Makes letters lowercase
                              • Counts every letter
                                   │
                                   ▼ 
                                (Sends the messy counts)
                             stats.py -> chars_dict_to_sorted_list
                              • Sorts biggest to lowest
                                   │
                                   ▼ 
                                    (Sends the neat list)
                             main.py -> print_report
                              • Skips spaces & symbols
                              • Prints the clean stats
                                   │
                                   ▼
                 The complete book report prints on screen
