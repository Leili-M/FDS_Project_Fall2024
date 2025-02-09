import streamlit as st

def main():
    st.set_page_config(page_title="FDS Project Report", layout="wide")
    
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Go to", ["PART1", "PART2", "PART3"])
    
    if page == "PART1":
        show_part1()
    elif page == "PART2":
        show_part2()
    elif page == "PART3":
        show_part3()
        
def show_part1():
    st.title("EDA")
    # PART 1.1
    st.write("Create 3 bar charts. For each bar chart draw the number of publications in a given year range. Do this for the ranges 1937-1950, 1950-1970, 1970-1990. Compare the three")
    st.image("1.1/output_1.1.png", caption="output_1.1")
    with st.container():
        st.markdown('<h3 style="color:#3674B5;">Publications (1937-1950)</h3>', unsafe_allow_html=True)
        st.write("The number of publications is relatively low.")
        st.write("There is some variation, with the highest peak reaching around 3 publications.")
        st.write("Some years have no publications.")
        
        st.markdown('<h3 style="color:#3674B5;">Publications (1950-1970)</h3>', unsafe_allow_html=True)
        st.write("There is a clear upward trend.")
        st.write("The number of publications increases significantly, especially after 1960.")
        st.write("By 1970, the number of publications exceeds 200.")
        
        st.markdown('<h3 style="color:#3674B5;">Publications (1970-1990)</h3>', unsafe_allow_html=True)
        st.write("A dramatic increase in the number of publications.")
        st.write("The number of publications continues to rise exponentially.")
        st.write("By 1990, the count reaches around 2700 publications.")

    # PART 1.1.2
    st.write("Create a bar chart of the number of references over the years.")
    st.image("1.1/output_1.1.2.png", caption="output_1.1.2")
    st.write(' The number of references significantly increases over time, particularly after the 1990s. Before 1980, the number of references per year is relatively low. A steady growth phase starts around the 1990s, increasing each year.', unsafe_allow_html=True)

    #PART 1.1.3
    st.write("Create a bar chart of the number of authors over the years.")
    st.image("1.1/output_1.1.3.png", caption="output_1.1.2")
    st.write(' The number of authors has shown a steady increase over the decades, particularly after 1990.Before 1970, the number of authors was relatively low, which aligns with the historical trend of individual researchers publishing more than collaborative teams.Around the 1990s, there is a noticeable rise in the number of authors per year.The number of authors peaks dramatically in the 2010s and 2020.', unsafe_allow_html=True)
   
    #PART 1.1.4
    st.write(" Find the Pearson correlation coefficient and Spearman Rank correlation coeffbetween the number of authors and number of references.")
    st.markdown('<h3 style="color:#3674B5;border:5px solid #3674B5;text-align:center;margin:40px;">Result is:<p> Pearson Coefficient is 0.056027878375202955 and Spearman Rank Correlation is 0.0872116655830498.</h3>', unsafe_allow_html=True)
    st.write("The Pearson correlation (0.056) suggests almost no linear relationship between the number of authors and references.")
    st.write("The Spearman correlation (0.087) indicates a slightly stronger but still weak monotonic relationship.")
             

        
    #PART 1.1.5
    st.write(" Find the Pearson correlation coefficient and Spearman Rank correlation coeffbetween the number of authors and number of references.")
    st.markdown('<h3 style="color:#3674B5;border:5px solid #3674B5;text-align:center;margin:40px;">Result is:<p> Pearson Coefficient is -0.0027965270825141553 and Spearman Rank Correlation is -0.01661606049149943</h3>', unsafe_allow_html=True)
    st.write("The Pearson correlation is almost zero correlation between the number of authors and the number of citations.Suggests that there is no significant linear relationship between the two variables.")
    st.write("The Spearman correlation is slightly negative but still very weak correlation.Indicates that there is almost no monotonic (rank-based) relationship between the number of authors and citations.")
    
    #PART 1.1.6
    st.write("Draw a bar chart of the title length over the years.")
    st.image("1.1/output_1.1.6.png", caption="output_1.1.2")
    st.write('From the 1940s to 2020, there is a clear upward trend in average title length.This suggests that research paper titles have gradually become longer over the decades.In earlier years (before 1950), title lengths were shorter and more varied, but after 1970, there is a steady increase.The 1930s to 1950s show large fluctuations in title length, with some years having very short average titles and others having extremely long ones.', unsafe_allow_html=True)

    #PART 1.1.7
    st.write("Draw a bar chart of the title length over the years.")
    st.image("1.1/output_1.1.7.png", caption="output_1.1.7")
    st.write('The largest and most prominent words include:"paper," "propose," "use," "present," "model," "problem," "proposed," "results."These words are commonly associated with academic research abstracts, reflecting the typical structure of research papers.', unsafe_allow_html=True)
    
    #PART 1.1.8
    st.write("**Pearson Correlation:**")
    st.write("- Pearson correlation measures linear relationships.")
    st.write("- A value of 0.2718 indicates a weak positive correlation between title length and the length of referenced paper titles.")
    st.write("- This suggests that papers with longer titles tend to reference other papers with longer titles, but the relationship is not strong.")
    st.write("- The correlation is not close to 0, so there is some level of connection, but many other factors likely influence title length.")
    
    st.write("**Spearman Correlation:**")
    st.write("- Spearman correlation measures monotonic relationships, meaning it detects increasing/decreasing trends even if they are not perfectly linear.")
    st.write("- The Spearman coefficient is slightly higher (0.2737) than Pearson, suggesting a weak but slightly stronger monotonic relationship.")
    st.write("- This means that as one paper's title length increases, its referenced papers also tend to have longer titles, though not in a perfectly linear way.")
    #PART 1.1.9
    # Table of authors
    st.subheader("Top Authors Based On Publications")
    author_data = {
        "Author": ["Wei Wang", "Wei Zhang", "Yang Liu", "Lei Zhang", "Wei Li", "Jun Wang", "Lei Wang", "Lajos Hanzo", "Wei Liu", "Jun Zhang"],
        "Publications": [950, 657, 629, 579, 559, 544, 519, 458, 456, 455]
    }
    st.markdown(
    """<style> table, th, td {
            border: 3px solid #3674B5 !important;
            border-collapse: collapse;
            padding: 8px;
        }
    </style>""",
    unsafe_allow_html=True
)
    st.table(author_data)

    #PART 1.1.10
    st.subheader("Top 10 Authors by Citations")
    citation_data = {
        "Author": ["David G. Lowe", "Hari Balakrishnan", "Scott Shenker", "Ian F. Akyildiz", "Michael I. Jordan", "Ion Stoica", "Chih-Jen Lin", "Takeo Kanade", "Deborah Estrin", "Vladimir Vapnik"],
        "Citations": [65344, 55096, 54164, 53654, 53448, 52890, 52302, 50743, 49925, 49755]
    }
    st.markdown(
        """<style>
            table, th, td {
                border: 3px solid #4DA1A9 !important;
                border-collapse: collapse;
                padding: 8px;
            }
        </style>""",
        unsafe_allow_html=True
    )
    st.table(citation_data)
    
    #PART 1.1.11
    st.subheader("Top 10 Papers by References")
    references_data = {
        "Paper ID": [371369, 780292, 104143, 214646, 484969, 223901, 302124, 707510, 325083, 538381],
        "Title": [
            "Comprehensive frequency-dependent substrate no...",
            "Time in Qualitative Simulation.",
            "Bibliography on cyclostationarity",
            "Fifty Years of MIMO Detection: The Road to Lar...",
            "An Exploration of Enterprise Architecture Rese...",
            "Structure and dynamics of molecular networks: ...",
            "The NP-completeness column: An ongoing guide",
            "Digital geometry",
            "Deep Learning: Methods and Applications",
            "Review: learning bayesian networks: Approaches..."
        ],
        "References": [759, 561, 412, 396, 394, 386, 363, 361, 343, 326]
    }
    st.markdown(
        """<style>
            table, th, td {
                border: 3px solid #66785F !important;
                border-collapse: collapse;
                padding: 8px;
            }
        </style>""",
        unsafe_allow_html=True
    )
    st.table(references_data)
    #PART 1.1.12
    st.subheader("Top 10 Papers by Citations")
    citations_data = {
        "Paper ID": [332760, 294527, 358174, 716671, 18485, 45248, 81801, 150727, 458466, 442067],
        "Title": [
            "Distinctive Image Features from Scale-Invarian...",
            "Bowling alone: the collapse and revival of Ame...",
            "LIBSVM: A library for support vector machines",
            "Random Forests",
            "Support-Vector Networks",
            "MapReduce: simplified data processing on large...",
            "A fast and elitist multiobjective genetic algo...",
            "A theory for multiresolution signal decomposit...",
            "ImageNet Classification with Deep Convolutiona...",
            "Histograms of oriented gradients for human det..."
        ],
        "Citations": [42508, 34288, 33016, 28679, 26114, 24381, 24245, 24182, 22884, 22795]
    }
    st.markdown(
        """<style>
            table, th, td {
                border: 3px solid #61A3BA !important;
                border-collapse: collapse;
                padding: 8px;
            }
        </style>""",
        unsafe_allow_html=True
    )
    st.table(citations_data)
    
    #PART 1.1.13
    st.image('1.1/output_1.1.13.png' , caption="output_1.1.13")
    st.write("The blue dots represent actual data points, where each dot corresponds to an author’s number of publications (X-axis) and total number of citations (Y-axis).The red line represents the linear regression model's fit, attempting to predict the number of citations based on the number of publications.The spread of points indicates significant variation in citation counts, even for authors with a similar number of publications.")
    st.write("R² (Coefficient of Determination) = 0.34 means that 34 percent of the variance in citations can be explained by the number of publications.This suggests a moderate but not strong relationship:There is some correlation between the number of publications and citations.However, 66 percent of citation variation is influenced by other factors not accounted for in this model.")
    
    #1.2 : Citation Network (Paper-Paper Network)
    st.title("Citation Network (Paper-Paper Network)")
    st.image("1.2/1.2.1.png" , caption="Citation Network")
    st.subheader("Clustering Coefficient Over Time")
    st.write("**Observations from the Graph:**")
    st.write("**Before 1970:** The clustering coefficient is near zero, indicating a sparse citation network with little interconnection.")
    st.write("**1970s Spike:** Around the early 1970s, a sharp increase in clustering coefficient is observed, peaking above 0.02.")
    st.write("This suggests that research papers started citing more interconnected works, leading to a more densely connected network.")
    st.write("**Post-1980 to 2000:**")
    st.write("- The clustering coefficient fluctuates but remains nonzero, indicating a more interconnected research landscape.")
    st.write("- Multiple peaks suggest the emergence of strongly cited sub-networks (e.g., influential research areas).")
    st.write("**Post-2000 Increase:**")
    st.write("- A gradual rise in clustering coefficient suggests that research has become increasingly interconnected.")
    st.write("- More papers cite well-established sources, forming tightly connected communities.")
    st.write("**Recent Peak (~2020):**")
    st.write("A significant jump suggests a shift towards highly interconnected citations.")
    st.subheader("Network Metrics")
    st.write("**Average Path Length = 11.29**")
    st.write("- This means that, on average, any two papers in the citation network are 11.29 citations apart.")
    st.write("- Suggests a moderate level of connectivity, but still requires many citation 'hops' to navigate the full network.")
    st.write("**Diameter = 29**")
    st.write("- The longest shortest path in the network is 29 steps.")
    st.write("- This indicates that while some research fields are tightly interconnected, others remain far apart, requiring multiple citations to link related works.")
    
    #PART 1.2.2 Co-authorship Network (Author-Author Network) need to run again
    st.title("Co-authorship Network (Author-Author Network)")
    
#     Why Do We Use Louvain for Community Detection?
# Louvain is one of the best algorithms for detecting communities in large networks because:Many community detection methods are too slow for large networks.
# Louvain optimizes modularity in a hierarchical way, making it much faster than other algorithms like Girvan-Newman or Spectral Clustering.
# It works well on graphs with millions of nodes and edges.
    #PART 1.2.3  Venue Network (Conference-Journal Network)
    st.title("Venue Network (Conference-Journal Network)")
    st.image("1.2/1.2.3.1.png")
    st.write("The histogram of degree distribution shows that most venues have a very low degree centrality.The majority of venues do not frequently cite other venues, meaning they are more isolated within their own research communities.A small number of venues have a higher degree, meaning they play a significant role in connecting different venues.")
    st.write('Measures how often a venue lies on the shortest path between other venues. The "human factors in computing systems" venue ranks highly, suggesting it acts as a bridge between different research domains.')
    st.write("- **IEEE Transactions on Pattern Analysis and Machine Intelligence:** This venue is frequently cited, indicating its influence in the academic community.")
    st.write("- **Human Factors in Computing Systems (High Betweenness):** It likely connects multiple disciplines, meaning that interdisciplinary research frequently passes through this journal.")
    st.write("- **Neural Information Processing Systems (High Closeness):** It has a strong reachability across the network, meaning that papers from various disciplines quickly find their way to this venue.")
    st.image("1.2/1.2.3.2.png")
    st.write("The number of new venue connections per year has dramatically increased after 2010, with a steep rise around 2015-2020.There was relatively little interdisciplinary citation activity before the 2000s.")

    #PART 1.2.4 Temporal Evolution of the Citation Network
    st.title("Temporal Evolution of the Citation Network")
    st.markdown("<h5>This section has done by a sample with fraction 0.05 </h5>",unsafe_allow_html=True)
    st.image("1.2/1.2.4.1.png")
    st.write("The density of the citation network fluctuates significantly across different years.There are sharp spikes in density, particularly around the 1950s and 1960s, followed by a decline in the later years.After 1980, the network density becomes much lower and relatively stable.")
    st.write("The spikes in density suggest bursts of citations within short timeframes. These could correspond to landmark papers or specific technological advancements that led to increased interconnections in the citation network.The decline after 1980 might indicate the expansion of academic literature, where papers are spread across a larger number of research domains, reducing the overall density.The stabilization in later years suggests a more distributed citation network, where papers are being cited across a broader field instead of forming dense clusters.")
    st.write("The papers with the highest in-degree values represent major breakthroughs that have significantly impacted research communities.Many of these top-cited papers correspond to computer vision and machine learning, reinforcing the dominance of AI-related research in recent citation patterns.")
    st.write("- The most highly cited papers include well-known research contributions, such as:")
    st.write("  - *Distinctive Image Features from Scale-Invariant Keypoints* (5841 citations, 2004)")
    st.write("  - *LIBSVM: A library for support vector machines* (5057 citations, 2011)")
    st.write("  - *Histograms of Oriented Gradients for Human Detection* (3279 citations, 2005)")
    st.write("  - *ImageNet Classification with Deep Convolutional Networks* (3242 citations, 2012)")
    st.write("  - *Random Forests* (3235 citations, 2001)")

    st.image("1.2/1.2.4.2.png")
    st.write("The fraction of new papers being integrated into the citation network fluctuates over time.In the early years (1940s–1960s), integration was unstable, showing rapid increases and decreases.From 1980 onwards, the integration fraction stabilized and increased, reaching its peak between 1990 and 2010.A notable decline in integration is visible in the most recent years.")

def show_part2():
    #PART 2
    #PART 2.1
    # Edges (Connections): An edge (connection) exists between two authors if they co-authored at least one paper together.
    st.title("Community Detection")
    st.write("Louvian Algorithm")
    community_data = {
        "Community": ["Community 1", "Community 2", "Community 3", "Community 4", "Community 5"],
        "Size": [116129, 66702, 45662, 34310, 29796],
        "Top Authors": [
            "Xing Zhou, Tao Fang, Lap-Pui Chau, Cyrus Shahabi, Shu-Yuen Didi Yao, Roger Zimmermann, Huaguang Zhang, Zhenwei Liu, Guang-Bin Huang, Zhanshan Wang...",
            "Genevi eve Paquin, Laurent Vuillon, Simonetta Balsamo, Gian–Luca Dei Rossi, Andrea Marin, Steven Euijong Whang, David Menestrina, Georgia Koutrika, Martin Theobald, Hector Garcia-Molina...",
            "Archana K. Singh, Hideki Asoh, Jocelyn Y. K. Aulin, Djordje Jeremic, Antoine Bossard, Keiichi Kaneko, Shietung Peng, Elon Rimon, Hiro Takahashi, Takeshi Kobayashi...",
            "Efraim Laksman, Håkan Lennerstad, Pietro Andreani, Ahmed Bader, Eylem Ekici, Daniele D. Giusto, Maurizio Murroni, Giulio Soro, Emilie Bosc, Patrick Le Callet...",
            "Olof Olsson, Philippe Hanhart, Touradj Ebrahimi, Elisabeth André, Peter Ingwersen, Chu-Ren Huang, Daniel Ferrés, Horacio Rodríguez, Hossein Sameti, Hisami Suzuki..."
        ]
    }
    st.markdown(
    """<style> table, th, td {
            border: 3px solid #3674B5 !important;
            border-collapse: collapse;
            padding: 8px;
        }
    </style>""",
    unsafe_allow_html=True
)
    st.table(community_data)
    # st.write("- **Community 1 (Size: 116129):** Xing Zhou, Tao Fang, Lap-Pui Chau, Cyrus Shahabi, Shu-Yuen Didi Yao, Roger Zimmermann, Huaguang Zhang, Zhenwei Liu, Guang-Bin Huang, Zhanshan Wang...")
    # st.write("- **Community 2 (Size: 66702):** Genevi eve Paquin, Laurent Vuillon, Simonetta Balsamo, Gian–Luca Dei Rossi, Andrea Marin, Steven Euijong Whang, David Menestrina, Georgia Koutrika, Martin Theobald, Hector Garcia-Molina...")
    # st.write("- **Community 3 (Size: 45662):** Archana K. Singh, Hideki Asoh, Jocelyn Y. K. Aulin, Djordje Jeremic, Antoine Bossard, Keiichi Kaneko, Shietung Peng, Elon Rimon, Hiro Takahashi, Takeshi Kobayashi...")
    # st.write("- **Community 4 (Size: 34310):** Efraim Laksman, Håkan Lennerstad, Pietro Andreani, Ahmed Bader, Eylem Ekici, Daniele D. Giusto, Maurizio Murroni, Giulio Soro, Emilie Bosc, Patrick Le Callet...")
    # st.write("- **Community 5 (Size: 29796):** Olof Olsson, Philippe Hanhart, Touradj Ebrahimi, Elisabeth André, Peter Ingwersen, Chu-Ren Huang, Daniel Ferrés, Horacio Rodríguez, Hossein Sameti, Hisami Suzuki...")
    st.markdown("<h4>Conclusion</h4>", unsafe_allow_html=True)
    st.write('Louvain community detection algorithm has identified clusters of authors based on their co-authorship relationships.Each "Community" represents a group of authors who are more( densely connected to each other than to the rest of the network.')

    st.write("Spectral clustering groups authors into distinct research communities based on their collaborations.")
    st.subheader("Spectral Clustering Communities")
    spectral_community_data = {
        "Community": ["Community 1", "Community 2", "Community 3", "Community 4", "Community 5"],
        "Size": [11081, 920, 921, 1013, 885],
        "Top Authors": [
            "Maria G. Koziri, Panos Papadopoulos, Nikos Tziritas, Antonios N. Dadaliaris, Thanasis Loukopoulos...",
            "Artur Zawadzki, Marek Gorgon, Chia-Yen Chen, Radim Sara, Chih-Lin Chi...",
            "Arber Murturi, Burak Kantarci, Sema Oktug, Nicholas R. Howe, Andreas Fischer...",
            "Jiancong Luo, Ishfaq Ahmad, Yu Sun, Rajesh M. Krishnaswamy, Kumar N. Sivarajan...",
            "J. Jesu Vedha Nayahi, V. Kavitha, Deepika Saini, Sanjeev Kumar, Fawang Liu..."
        ]
    }
    st.table(spectral_community_data)
    st.write("Hierarchical Clustering Communities")
    hierarchical_community_data = {
        "Community": ["Community 1", "Community 2", "Community 3", "Community 4", "Community 5"],
        "Size": [2938, 15, 11, 28, 12],
        "Top Authors": [
            "Maria G. Koziri, Panos Papadopoulos, Nikos Tziritas, Antonios N. Dadaliaris, Thanasis Loukopoulos...",
            "Cheryl H. Porter, Chris Villalobos, Dean P. Holzworth, Roger Nelson, Jeffrey W. White...",
            "Seydou Traoré, Abdrahamane Anne, Aly Khalifa, S. Bosomprah, F. Caroline...",
            "Rolf Apweiler, Terri K. Attwood, Amos Marc Bairoch, Alex Bateman, Ewan Birney...",
            "Lambert Schaelicke, John B. Carter, Wilson C. Hsieh, Mark R. Swanson, Lixin Zhang..."
        ]
    }
    st.markdown(
    """<style> table, th, td {
            border: 3px solid #3674B5 !important;
            border-collapse: collapse;
            padding: 8px;
        }
    </style>""",
    unsafe_allow_html=True
)
    st.table(hierarchical_community_data)
    st.image('2/2.1.png',caption="dendogram")
    st.write("Louvain Clustering Coefficient: 0.6703")
    st.write("Spectral Clustering Coefficient: 0.5786")
    st.write("Hierarchical Clustering Coefficient: 0.9597")
    
    st.write("Clustering Algorithm Comparison:")
    st.write("- Louvain: 0.6703")
    st.write("- Spectral: 0.5786")
    st.write("- Hierarchical: 0.9597")
    
    st.write("Best Clustering Algorithm Based on Clustering Coefficient: Hierarchical")
    st.write("Louvain clustering is optimized for modularity and often performs well in large-scale networks.")
    st.write("A 0.6703 coefficient suggests that the detected communities have a moderate level of internal connectivity.")
    
    st.write("Spectral clustering operates by leveraging the eigenvalues of the adjacency matrix.")
    st.write("A coefficient of 0.5786 is lower than Louvain, indicating that the detected clusters are less tightly connected than those found by Louvain.")
    
    st.write("Hierarchical clustering groups nodes based on similarity in a recursive manner.")
    st.write("A 0.9597 coefficient suggests that the communities detected are very strongly connected, meaning the hierarchical structure effectively captures natural clusters.")
    st.write("If the dataset size increases significantly, Louvain might still be preferred due to its scalability, while Hierarchical Clustering could become computationally expensive.")
    #PART 2.2 Naming the Communities
    st.title("Naming the Communities")
    st.write("These keywords have been automatically extracted using BERT-based embeddings, meaning they are not just random words but contextually important terms found in the paper.The extracted keywords successfully summarize each paper’s topic.They provide a quick way to understand what a paper is about without reading the full abstract. The keywords highlight core research areas, making it easier to categorize, cluster, or search for similar papers.")
    st.title("Combined Keywords")
    paper_data = {
        "ID": [987231, 79954, 567130, 500891],
        "Title": [
            "Slice-based parallelization in HEVC encoding...",
            "MIDAS: A Middleware for Information Systems wi...",
            "Automatically controlled pan-tilt smart camera...",
            "Particle Filter for Visual Tracking Using Mult..."
        ],
        "Combined Keywords": [
            "alternative hevc, hevc, hevc using, paralleli...",
            "middleware information, qos concerns, isolati...",
            "analysis camera, smart camera, camera device,...",
            "particle filter, tracking using, visual track..."
        ]
    }
    st.table(paper_data)
    
    st.title("Community Keywords ")
    community_data = {
        "Community": ["Community 0", "Community 1", "Community 2", "Community 3", "Community 4"],
        "Combined Keywords": [
            "matrix multiplication, hevc using, matrix powers, adaptation distributed, overhead hevc, parallel algorithms, scalable parallel, parallelization hevc, based parallelization, video coding...",
            "middleware information, qos concerns, isolation concurrency, middleware, midas middleware, storage engine, systems qos, database servers, minimizes transactions, concurrency...",
            "analysis camera, smart camera, camera fpga, camera device, fpga based, tracking moving, tilt smart, controlled camera, position camera, orientation camera...",
            "particle filter, tracking using, visual tracking, tracking, bayesian filtering, visual track, track ing, cameras overlapping, multiple cameras...",
            "crowdsourcing service, crowdsourcing development, service, workflow crowdsourcing, mobile crowdsourcing, reference model, crowdsourcing services, crowdsourcing, model crowdsourcing..."
        ]
    }
    st.table(community_data)
    st.title("Associated Community")
    paper_data = {
        "ID": [987231, 79954, 567130],
        "Paper ID": ["3e5ef05b-bb89-4717-bfc3-74a467529ded", "653894e3-b581-412c-ae3f-71d267b0ea9d", "0ba8b19f-9659-453f-8deb-50b87e26e41f"],
        "Title": [
            "Slice-based parallelization in HEVC encoding...",
            "MIDAS: A Middleware for Information Systems wi...",
            "Automatically controlled pan-tilt smart camera..."
        ],
        "Community": [0, 1, 2]
    }
    st.table(paper_data)

    st.title("Community Keywords")
    paper_data = {
        "ID": [987231, 79954, 567130, 500891, 55399, 135049, 733378],
        "Paper ID": [
            "3e5ef05b-bb89-4717-bfc3-74a467529ded", "653894e3-b581-412c-ae3f-71d267b0ea9d", 
            "0ba8b19f-9659-453f-8deb-50b87e26e41f", "f12c84ba-82a9-4835-b5fa-5e6715b1b6b3", 
            "5d197014-1fbb-40d8-8223-378dea0d4a30", "7790685d-525b-4f64-bd58-12d8cea683c8", 
            "08f4b403-7400-48d6-981b-6e76424ac967"
        ],
        "Title": [
            "Slice-based parallelization in HEVC encoding...",
            "MIDAS: A Middleware for Information Systems wi...",
            "Automatically controlled pan-tilt smart camera...",
            "Particle Filter for Visual Tracking Using Mult...",
            "A reference model for crowdsourcing as a service",
            "A Landweber algorithm for 3D confocal microsco...",
            "Computing group cardinality constraint solutio..."
        ],
        "Combined Keywords": [
            "matrix multiplication, hevc using, matrix pow...",
            "middleware information, qos concerns, isolati...",
            "analysis camera, smart camera, camera fpga...",
            "particle filter, tracking using, visual track...",
            "crowdsourcing service, crowdsourcing developm...",
            "microscopy, deconvolution introduced, landweb...",
            "minimization logistic, constraint, cardinalit..."
        ]
    }
    st.table(paper_data)
    st.title("Aggregation:")
    st.write("The goal is to assign relevant keywords to each community, which can be used to understand the main research topics within those communities.")
    st.write("Each research paper is associated with one or more communities based on its authors. Since authors are clustered into research communities, a paper written by multiple authors might belong to multiple communities. To keep track of this relationship, we create a mapping where each paper ID is linked to the communities it belongs to.")
    
    st.write("For example:")
    st.write("- Paper A is written by authors from Community 0 and Community 1.")
    st.write("- Paper B is written by authors from Community 1 and Community 2.")
    st.write("This mapping ensures that each paper contributes to the research themes of all its associated communities.")
    
    st.write("Each paper contains a title and an abstract, which are rich sources of information about its topic. To extract meaningful keywords from these text fields, we use KeyBERT, a model that identifies the most important words and phrases in a given text.")
    
    st.write("For example, a paper titled 'Advances in Deep Learning for Natural Language Processing' might have extracted keywords like:")
    st.write("- Deep Learning")
    st.write("- Natural Language Processing")
    st.write("- Neural Networks")
    
    st.write("These keywords represent the core research areas of the paper. Once the keywords for a paper are extracted, they are distributed to all the communities the paper is associated with. This ensures that each community gets insights into the topics covered by the papers written by its authors.")
    
    st.write("For instance:")
    st.write("- Paper A has keywords: 'Deep Learning', 'AI', 'Neural Networks'")
    st.write("- Paper A belongs to Community 0 and Community 1.")
    st.write("- These keywords are added to both Community 0 and Community 1.")
    
    st.write("Since multiple papers in the same community might have overlapping keywords, we use a set to store keywords instead of a list. A set automatically removes duplicate entries, ensuring that each keyword appears only once per community.")
    
    st.write("For example:")
    st.write("If Community 1 receives keywords from multiple papers:")
    st.code('{"Deep Learning", "AI", "Neural Networks", "AI", "Deep Learning"}')
    st.write("The final set for Community 1 will be:")
    st.code('{"Deep Learning", "AI", "Neural Networks"}')
    community_keywords_data = {
        "Community": ["Community 0", "Community 1", "Community 2", "Community 3", "Community 4", "Community 5", "Community 6", "Community 7"],
        "Keywords": [
            "matrix multiplication, hevc using, matrix powers, adaptation distributed, overhead hevc, parallel algorithms, scalable parallel, parallelization hevc, based parallelization, video coding...",
            "middleware information, qos concerns, isolation concurrency, middleware, midas middleware, storage engine, systems qos, database servers, minimizes transactions, concurrency...",
            "analysis camera, smart camera, camera fpga, camera device, fpga based, tracking moving, tilt smart, controlled camera, position camera, orientation camera...",
            "particle filter, tracking using, visual tracking, tracking, bayesian filtering, visual track, track ing, cameras overlapping, multiple cameras...",
            "crowdsourcing service, crowdsourcing development, service, workflow crowdsourcing, mobile crowdsourcing, reference model, crowdsourcing services, crowdsourcing, model crowdsourcing...",
            "microscopy, deconvolution introduced, landweber algorithm, 3d confocal, deconvolution algorithm, microscopy deconvolution, deconvolution, iterative deconvolution, microscopy restoration, confocal microscopy...",
            "minimization logistic, constraint, cardinality constraint, features weighted, restoring contrast, contrast restoration, degraded images, fog degraded, constraint weighted, fog...",
            "auditory cortex, cortex deep, speech reconstruction, human auditory, deep neural..."
        ]
    }
    st.table(community_keywords_data)
    st.title("Assign a name")
    st.write("Each community has a set of unique keywords extracted from the papers authored by its members.")
    st.write("The most frequently occurring key terms represent the central research themes of the community.")
    st.write("The keywords are grouped into broader categories such as Machine Learning, NLP, Computer Vision, etc.")
    st.write("These topics are aligned with known research domains.")
    paper_community_data = {
        "Paper ID": [987231, 79954, 567130, 500891, 55399, 135049, 733378, 732057, 51333],
        "Keywords": [
            "matrix multiplication",
            "middleware information",
            "analysis camera",
            "particle filter",
            "crowdsourcing service",
            "microscopy",
            "minimization logistic",
            "auditory cortex",
            "infection"
        ]
    }
    st.table(paper_community_data)

    #PART 2.3
    st.image('2/2.3.png',caption="clustring")
    st.write("I used the K-Means clustering algorithm for clustering the paper embeddings.")
    st.write("Each point represents a research paper.")
    st.write("Spatial proximity between points indicates semantic similarity (papers that are closer together are more related).")
    st.write("Clusters are well-formed, indicating a meaningful separation of research topics.")
    st.write("Some overlapping regions suggest interdisciplinary research areas or potential improvements in clustering methodology.")
    st.write("Larger clusters may correspond to broad topics, while smaller clusters could indicate specialized fields.")
    
    st.write("Conclusion:")
    
    st.write("DBI measures cluster compactness and separation.")
    st.write("Lower values indicate better clustering because it means that clusters are well-separated and compact.")
    st.write("A DBI score of 4.2225 is quite high, meaning:")
    st.write("- The clusters might be overlapping too much.")
    st.write("- The clusters might not be well-separated.")
    
    st.write("Silhouette Score measures how similar points are within their cluster vs. other clusters.")
    st.write("Range:")
    st.write("- +1 → Perfect clusters (tight & well-separated)")
    st.write("- 0 → Overlapping clusters")
    st.write("- -1 → Bad clustering (points assigned to the wrong cluster)")
    
    st.write("A Silhouette Score of 0.0314 is extremely low, indicating:")
    st.write("- The clusters overlap significantly.")
    st.write("- K-Means might not be the best algorithm for your data.")
    st.write("Jaccard Similarity measures how similar two sets are (intersection over union).-0.0117 : Extremely low overlap, meaning:Clustering does not align well with venues.")

def show_part3():
    st.title("Regressor") 
    st.write("In this section, we aimed to identify the best regression model for our dataset by utilizing a combination of **AutoML** and **GridSearch** techniques.")
    
    # st.write("#### **Dataset and Preprocessing**")
    st.write("- We used a dataset containing **12,000** samples for training and **3,000** for testing.")
    st.write("- To extract meaningful representations from the text data, we employed **BERT-based sentence embeddings**, which effectively capture the semantic relationships between words.")
    
    # st.write("#### **Model Selection Approach**")
    st.write("To find the most effective regression model, we explored two approaches:")
    st.write("1. **AutoML using TPOT** – An automated machine learning pipeline optimization tool that systematically searches for the best model and hyperparameters.")
    st.write("2. **GridSearch** – A traditional hyperparameter tuning method that evaluates predefined parameter combinations to optimize model performance.")
    
    st.write("#### **Best Performing Model**")
    st.write("Both approaches independently determined that **Random Forest Regression** was the most effective model for our dataset.")
    st.write("This indicates that an ensemble-based method, which leverages multiple decision trees to improve accuracy and reduce overfitting, provided the best generalization to unseen data.")
    st.write("## Result: ##")
    result_data = {
        "Paper ID": [764015, 822808, 836090, 60912, 978063, 576953, 585731, 615581, 475637, 839929, 913465, 578924],
        "Actual Citations": [1.0, 20.0, 50.0, 122.0, 50.0, 1.0, 50.0, 0.0, 1.0, 0.0, 2.0, 2.0],
        "Predicted Citations": [48.429339, 47.662775, 34.755575, 40.928889, 63.006181, 38.012007, 42.905927, 33.234957, 36.613135, 30.971990, 32.501050, 52.305242]
    }
    st.write("### Random Forest Regression Results")
    st.markdown(
    """<style> table, th, td {
            border: 3px solid #3674B5 !important;
            border-collapse: collapse;
            padding: 8px;
        }
    </style>""",
    unsafe_allow_html=True
)
    st.table(result_data)

    evaluation_metrics = {
        "Metric": ["RMSE (Root Mean Squared Error)", "MAE (Mean Absolute Error)", "R² Score"],
        "Value": [440.1746, 93.9885, -0.0224],
        "Interpretation": [
            "High RMSE indicates **large deviations** between predicted and actual citation counts.",
            "On average, predictions deviate by **94 citations** from actual values.",
            "A negative R² suggests the model **performs worse than a simple mean predictor**, meaning **very weak predictive power**."
        ]
    }
    
    st.table(evaluation_metrics)

    #Reg2
    st.write("### XGBoost Regression Results")
    xgboost_result_data = {
        "Paper ID": [764015, 822808, 836090, 60912, 978063, 576953, 585731, 615581, 475637, 839929, 913465, 578924, 443603, 980326],
        "Actual Citations": [1.0, 20.0, 50.0, 122.0, 50.0, 1.0, 50.0, 0.0, 1.0, 0.0, 2.0, 2.0, 2.0, 0.0],
        "Predicted Citations": [2.062268, 7.706326, 10.979347, 20.424091, 12.171082, 5.304145, 8.939227, 6.703262, 11.065205, 2.062268, 5.093034, 28.788328, 12.332393, 2.062268]
    }
    st.table(xgboost_result_data)
    st.write("### XGboost Regression Evaluation Metrics")

    XGBoost_evaluation_metrics = {
    "Metric": ["RMSE (Root Mean Squared Error)", "MAE (Mean Absolute Error)", "R² Score"],
    "Value": [123.1483, 32.8007, -0.0304],
    "Interpretation": [
        "The model's **prediction error** is significantly lower than previous models.",
        "On average, predictions deviate by **~33 citations** from actual values.",
        "**Slightly negative R²** suggests **poor model performance**, though better than before."
    ]
}

    st.table(XGBoost_evaluation_metrics)


    #REG3
    st.write("### LightGBM Regression Results")
    lightgbm_result_data = {
        "Paper ID": [764015, 822808, 836090, 60912, 978063, 576953, 585731, 615581, 475637, 839929, 913465, 578924, 443603, 980326, 766729, 492331],
        "Actual Citations": [1.0, 20.0, 50.0, 122.0, 50.0, 1.0, 50.0, 0.0, 1.0, 0.0, 2.0, 2.0, 2.0, 0.0, 2.0, 2.0],
        "Predicted Citations": [2.084499, 12.957464, 8.402867, 12.507732, 12.541244, 2.859069, 9.238611, 5.094810, 9.939477, 2.084499, 13.601302, 29.186782, 11.867864, 2.084499, 12.925098, 8.531064]
    }
    st.table(lightgbm_result_data)
    st.write("### LightGBM Regression Evaluation Metrics")

    lightgbm_evaluation_metrics = {
    "Metric": ["RMSE (Root Mean Squared Error)", "MAE (Mean Absolute Error)", "R² Score"],
    "Value": [123.4998, 32.8441, -0.0363],
    "Interpretation": [
        "The prediction error remains comparable to XGBoost, with a **slightly higher RMSE** than XGBoost (123.15).",
        "Mean absolute error is **almost identical** to XGBoost (32.8007), suggesting similar average prediction deviation.",
        "Slightly lower than XGBoost (-0.0304), indicating a **marginal decrease** in the model's ability to explain variance."
    ]
}

    st.table(lightgbm_evaluation_metrics)

    
    



if __name__ == "__main__":
    main()
# Louvain Clustering Coefficient: 0.6696