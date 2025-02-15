# 🚀 Comparative Analysis of Algorithms for Maximal k-Plex Enumeration over Real-world Graphs

📊 **Comparative Analysis of MPE** - A research project on MPE performance evaluation.

![Demo](https://github.com/thanhtritrang/Comparative-analysis-of-MPE/blob/main/images/chart.png)
![Demo](https://github.com/thanhtritrang/Comparative-analysis-of-MPE/blob/main/images/all.png)
---

## 📌 Introduction

This project focuses on analyzing the performance of **MPE** (Maximal k-Plex Enumeration) problem using various methods. The goal is to evaluate and compare algorithms on different datasets.

We sincerely thank the authors who have published the source code of the algorithms used in this study. Their contributions have greatly facilitated our research and analysis.
---

## 🔧 Installation

### System Requirements
- Python 3.x
- **Libraries**: NumPy, Pandas, Matplotlib
- **Algorithms**: PlexEnum, SAPE, D2K, ListPlex, FP, GP, CPlex
- **Datasets**: celegansneural, jazz, lastfm_asia_edges, ca-GrQc, wiki-Vote, as-caida20071105, p2p-Gnutella31, email-EuAll, soc-Epinions1, hollywood-2009, com-dblp.ungraph, road-belgium-osm, com-youtube.ungraph, twitter_combined, amazon0505, web-Google, road_usa, soc-LiveJournal1, soc-orkut, facebook_combined, karate_edges

### Command Explanations:
- --app        # Path to the algorithm
- --time       # Maximum execution time in seconds
- --data_path  # Path to dataset directory
- --k          # a positive integer representing the degree to which a k-plex deviates from a clique.
- --q          # a positive integer specifying the minimum vertices in a maximal k-plex.

### Installation Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/thanhtritrang/Comparative-analysis-of-MPE.git
   cd Comparative-analysis-of-MPE
   ```
2. **Run Algorithm of Enplex**:
   ```bash
    python main.py --app "algorithms/faplex/enplex" --time 86400 --data_path "datasets/bin/" --k "2 3 4 5" --q "10 20 30 50 100"
   ```
3. **Run Algorithm of SAPE**:
   ```bash
    python main.py --app "algorithms/KPLEX-WORK/max_kplex" --time 86400 --data_path "datasets/txt/" --k "2 3 4 5" --q "10 20 30 50 100"
   ```
4. **Run Algorithm of FP**:
   ```bash
    python main.py --app "algorithms/kplexEnum/kplexes" --time 86400 --data_path "datasets/bin/" --k "2 3 4 5" --q "10 20 30 50 100"
   ```
5. **Run Algorithm of ListPlex**:
   ```bash
    python main.py --app "algorithms/ListPlex/pro2/listPlex" --time 86400 --data_path "datasets/txt/" --k "2 3 4 5" --q "10 20 30 50 100"
   ```
6. **Run Algorithm of PlexEnum**:
   ```bash
    python main.py --app "algorithms/Maximal-kPlex/Sequential/PlexEnum" --time 86400 --data_path "datasets/bin/" --k "2 3 4 5" --q "10 20 30 50 100"
   ```
7. **Run Algorithm of D2K**:
   ```bash
    python main.py --app "algorithms/parallel_enum/text_ui" --time 86400 --data_path "datasets/nde/" --k "2 3 4 5" --q "10 20 30 50 100"
   ```
8. **Run Algorithm of GP**:
   ```bash
    python main.py --app "algorithms/GP_Kplex/BinaryOptimizeWithPrunNot" --time 86400 --data_path "datasets/txt/" --k "2 3 4 5" --q "10 20 30 50 100"
   ```
---
## 🌟 Key Features

✅ Performance analysis of MPE on multiple datasets 🔍  
✅ Data visualization with charts 📊  
✅ Algorithm comparison based on various criteria ⚖️  
✅ Support for multi-core CPU execution 🖥️  

---

## 📊 Results Demo

![Demo](https://github.com/thanhtritrang/Comparative-analysis-of-MPE/blob/main/images/result.png)

---

## 🤝 Contributing

We welcome contributions from the community! If you would like to contribute:
1. Fork this repository.
2. Create a new branch for your feature: `git checkout -b feature-new-feature`.
3. Commit your changes: `git commit -m "Add new feature"`.
4. Push to the new branch: `git push origin feature-new-feature`.
5. Create a **Pull Request** on GitHub.

---

## 📬 Contact

📧 Email: [tritrang88@gmail.com](mailto:tritrang88@gmail.com)  
📌 GitHub: [@thanhtritrang](https://github.com/thanhtritrang)  
🌐 Website: [thanhtritrang.github.io/resume](https://thanhtritrang.github.io/resume)  

---

## ⚖️ License

© 2025 **Comparative Analysis of MPE**. This project is licensed under the MIT License.

---

🔥 _Thank you for your interest in this project! If you find it useful, please give us a ⭐ on GitHub!_ 🚀
