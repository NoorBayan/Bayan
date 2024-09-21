# Bayan: Arabic Poetry Treebank for Syntactic Analysis

 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Bayan/main/images/BayanLogo.png" width = "200px"/>
 </p>
 
## Overview

**Bayan** is an innovative and fully annotated treebank dedicated to the syntactic analysis of Arabic poetry. This project aims to enhance the understanding of the linguistic structure of classical and modern Arabic poems by providing a rich and detailed syntactic treebank. Whether you're a linguist, a computer scientist, or a poetry enthusiast, Bayan offers a unique platform for exploring the beauty and complexity of Arabic verse.

### Features:
- **Detailed Syntactic Annotation**: Comprehensive syntactic trees for each poem, following the rules of Arabic grammar.
- **Wide Range of Poems**: Covers a variety of classical and modern Arabic poetry, highlighting different linguistic structures.
- **Search and Filter**: Easily search for poems by poet, era, or specific linguistic features.
- **Educational Tool**: A resource for students and researchers interested in Arabic syntax, morphology, and poetic structure.

---

## Data Description
Bayan provides a richly layered dataset, each layer offering a unique level of linguistic analysis. This multi-dimensional structure allows for a detailed examination of Arabic poetry, making it a valuable resource for researchers, linguists, and AI practitioners alike. The dataset is organized into three core layers, each focusing on a specific aspect of the text:

1. **Poetic Layer**:  
   This layer encapsulates the **metadata** and contextual information about each poem. It includes:
   - **Poem details**: Title, genre, and a brief description of the poem.
   - **Prosodic information**: Meter (Bahrs) used in the poem, along with rhyme schemes and rhythmic patterns.
   - **Historical context**: Era or period in which the poem was written, providing cultural and historical background.
   - **Poet information**: Detailed biographical data on the poet, including their era, style, and influence in the realm of Arabic literature.
   - **Poetic theme**: The subject matter or central theme of the poem, which could range from love, wisdom, and praise to philosophical and spiritual reflections.
   
2. **Orthographic Layer**:  
   This layer provides detailed **spelling and textual information**. It focuses on:
   - **Text normalization**: Ensures the Arabic text is standardized for accurate analysis, handling variations in spelling, diacritics, and punctuation.
   - **Script forms**: Offers insights into orthographic forms, including handling classical Arabic spelling variations and script styles.
   - **Diacritization**: In-depth vowel markings and other orthographic features, ensuring the text aligns with the standards of classical and modern Arabic writing.

3. **Morphological Layer**:  
   In this layer, Bayan dives into the **word-level analysis**, offering detailed morphological breakdowns of each word in the poem:
   - **Root and pattern extraction**: The system identifies the root (جذر) and morphological pattern (وزن) for every word, a fundamental feature in Arabic linguistics.
   - **Part-of-speech tagging**: Each word is labeled with its part of speech (noun, verb, adjective, etc.), along with morphological attributes such as gender, number, case, mood, and definiteness.
   - **Derivational and inflectional analysis**: Detailed analysis of word derivation and inflection, revealing patterns of verb conjugations, noun plurals, and adjective forms.
   - **Morphological glossing**: Includes glosses for non-trivial words, providing a clear understanding of meanings across different contexts.

4. **Syntactic Layer**:  
   The final layer provides a **full syntactic analysis**, mapping out the grammatical relationships between words within each line and verse. This includes:
   - **Dependency parsing**: Shows the syntactic roles of words and their relations to each other (e.g., subject, object, modifier).
   - **Phrase structure**: Illustrates how individual words combine into phrases (noun phrases, verb phrases, etc.) to form complex syntactic units.
   - **Embedded clauses**: Accounts for the nested structures and subordinate clauses that contribute to the complexity of Arabic sentence construction.
   - **Ellipsis and pro-drop phenomena**: Highlights instances where certain words or pronouns are implied or omitted but understood from context, reflecting the unique syntactic characteristics of Arabic poetry.

Together, these layers provide a comprehensive and nuanced linguistic analysis of Arabic poetry, allowing users to explore everything from high-level prosodic structures to fine-grained syntactic relations. Each layer is designed to complement the others, offering a cohesive framework for both linguistic research and advanced AI applications.

---

## Methodology

The Bayan treebank was developed through a structured, four-phase process, ensuring high-quality linguistic data:

 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Bayan/main/images/BayanMethodology.png" width = "400px"/>
 </p>
 
### Phase 1: Data Selection
The initial data for Bayan was selected from the **Quranic Treebank**, a well-established treebank for Classical Arabic. This provided a solid linguistic foundation for the syntactic structures required for analyzing Arabic poetry.

### Phase 2: Fine-tuning the Linguistic Model
In this stage, the **Gemini** model was fine-tuned using selected data from the Quranic Treebank. This model serves as the core for syntactic analysis and linguistic feature extraction in Bayan.

### Phase 3: Building the Bayan Dataset
The Bayan treebank was constructed based on the refined model. This involved curating a selection of Arabic poems, followed by detailed annotation of the syntactic, morphological, and orthographic structures.

### Phase 4: Validation and Evaluation
The final step involved validating the accuracy of the Bayan dataset. This was done through automatic grammar-based algorithms that ensured the syntactic annotations were consistent with the linguistic rules of Arabic.

---

## Usage

Bayan offers various functionalities, including:
- **Treebank Exploration**: Browse and explore the syntactic structure of poems.
- **Search Tool**: Use linguistic queries to search specific poems by syntactic features.
- **Custom Annotations**: Add or modify annotations to suit research needs.

---

## Explore Bayan on Google Colab

To explore the full details of the **Bayan Treebank** and interact with its extensive features, access our interactive Google Colab notebook. This notebook provides an easy-to-use interface for searching, analyzing, and learning more about the Diwan dataset.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1c2AsPfdwj4ELEypTEmsSTewtVQ8MVXP3?usp=drive_link)

 <p align="center">
   <img src = "https://raw.githubusercontent.com/NoorBayan/Bayan/main/images/BayanColab.png" width = "800px"/>
 </p>

### Steps to Use Bayan on Google Colab:

1. **Run the first cell** by clicking the "Run" button to load the necessary files and libraries.
2. **Execute the notebook**, and dropdown menus will appear with various poetry categories. You can experiment by selecting different options, and the corresponding poetic data will be displayed based on your choices.
3. You can explore **additional features** of the Diwan dataset by accessing the main menu on the left side of the notebook interface.
3. You can explore **additional features** of the Diwan dataset by accessing the main menu on the left side of the notebook interface.
4. 
---

## Contribution

We welcome contributions! If you would like to contribute to Bayan, feel free to submit a pull request or open an issue.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and open a pull request.

## Future Plans
- **Expanding the corpus**: Adding more poems from different eras and poets.
- **Enhanced Visualization**: Interactive and dynamic syntax tree exploration.
- **Semantic Analysis**: Incorporating semantic layers to complement syntactic annotations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
