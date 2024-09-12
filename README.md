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

## Data Description

Bayan consists of three fundamental layers, each providing a distinct level of linguistic analysis:

1. **Poetic Layer**: Contains metadata and information specific to the poem. The table below outlines the details of this layer.
   
<table>
    <thead>
        <tr>
            <th>No.</th>
            <th>Column</th>
            <th>Description-Arabic</th>
            <th>Description-English</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Tid</td>
            <td>عداد تسلسلي لصفوف الجدول</td>
            <td>Sequence counter for table rows</td>
        </tr>
        <tr>
            <td>2</td>
            <td>sentence_id</td>
            <td>عداد تسلسلي لجمل الكوربس</td>
            <td>Serial counter for sentences in the corpus/treebank</td>
        </tr>
        <tr>
            <td>3</td>
            <td>sentence_word</td>
            <td>عداد تسلسلي لكلمات كل جملة من جمل الكوربس</td>
            <td>Serial counter for the word in each sentence within the corpus/treebank</td>
        </tr>
        <tr>
            <td>4</td>
            <td>token_id</td>
            <td>عداد تسلسلي لتوكن كل كلمة من كلمات كل جملة من جمل الكوربس</td>
            <td>Serial counter for tokens of each word for each sentence in the corpus/treebank</td>
        </tr>
        <tr>
            <td>5</td>
            <td>location</td>
            <td>ترميز لموقع كل توكن وفق الترميز القرآني (التوكن: الكلمة: الآية: السورة)</td>
            <td>Code for encoding each token location in Quran (token: word: verse: surah/chapter)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>chapter_id</td>
            <td>عداد تسلسلي لسور القران الكريم المتكون من 114 سورة</td>
            <td>Serial counter for the surah/chapter in Quran, which consists of 114 surahs/chapters</td>
        </tr>
        <tr>
            <td>7</td>
            <td>verse_id</td>
            <td>عداد تسلسلي لآيات كل سورة في القران الكريم</td>
            <td>Serial counter of the verses in each surah/chapter in Quran</td>
        </tr>
        <tr>
            <td>8</td>
            <td>word_id</td>
            <td>عداد تسلسلي لكلمات كل آية في القران الكريم</td>
            <td>Serial counter of each word in each verse in Quran</td>
        </tr>
        <tr>
            <td>9</td>
            <td>tok_id</td>
            <td>عداد تسلسلي لتوكن كل كلمة في القران الكريم</td>
            <td>A serial counter for tokens in each word in Quran</td>
        </tr>
        <tr>
            <td>10</td>
            <td>imlaai_token</td>
            <td>الرسم الإملائي</td>
            <td>Imlaai script of the token</td>
        </tr>
        <tr>
            <td>11</td>
            <td>imlaai_unicode</td>
            <td>الرسم الإملائي بترميز يونيكود</td>
            <td>The Unicode of Uthmani script for each token</td>
        </tr>
        <tr>
            <td>12</td>
            <td>phonetic</td>
            <td>الترميز الصوتي للكلمات</td>
            <td>Phonetic encoding for each word</td>
        </tr>
    </tbody>
</table>

2. **Orthographic Layer**: This layer provides detailed information about the orthography and script used in the poems. The table below outlines the relevant fields.
<table>
    <thead>
        <tr>
            <th>No.</th>
            <th>Column</th>
            <th>Description-Arabic</th>
            <th>Description-English</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Tid</td>
            <td>عداد تسلسلي لصفوف الجدول</td>
            <td>Sequence counter for table rows</td>
        </tr>
        <tr>
            <td>2</td>
            <td>sentence_id</td>
            <td>عداد تسلسلي لجمل الكوربس</td>
            <td>Serial counter for sentences in the corpus/treebank</td>
        </tr>
        <tr>
            <td>3</td>
            <td>sentence_word</td>
            <td>عداد تسلسلي لكلمات كل جملة من جمل الكوربس</td>
            <td>Serial counter for the word in each sentence within the corpus/treebank</td>
        </tr>
        <tr>
            <td>4</td>
            <td>token_id</td>
            <td>عداد تسلسلي لتوكن كل كلمة من كلمات كل جملة من جمل الكوربس</td>
            <td>Serial counter for tokens of each word for each sentence in the corpus/treebank</td>
        </tr>
        <tr>
            <td>5</td>
            <td>location</td>
            <td>ترميز لموقع كل توكن وفق الترميز القرآني (التوكن: الكلمة: الآية: السورة)</td>
            <td>Code for encoding each token location in Quran (token: word: verse: surah/chapter)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>chapter_id</td>
            <td>عداد تسلسلي لسور القران الكريم المتكون من 114 سورة</td>
            <td>Serial counter for the surah/chapter in Quran, which consists of 114 surahs/chapters</td>
        </tr>
        <tr>
            <td>7</td>
            <td>verse_id</td>
            <td>عداد تسلسلي لآيات كل سورة في القران الكريم</td>
            <td>Serial counter of the verses in each surah/chapter in Quran</td>
        </tr>
        <tr>
            <td>8</td>
            <td>word_id</td>
            <td>عداد تسلسلي لكلمات كل آية في القران الكريم</td>
            <td>Serial counter of each word in each verse in Quran</td>
        </tr>
        <tr>
            <td>9</td>
            <td>tok_id</td>
            <td>عداد تسلسلي لتوكن كل كلمة في القران الكريم</td>
            <td>A serial counter for tokens in each word in Quran</td>
        </tr>
        <tr>
            <td>10</td>
            <td>imlaai_token</td>
            <td>الرسم الإملائي</td>
            <td>Imlaai script of the token</td>
        </tr>
        <tr>
            <td>11</td>
            <td>imlaai_unicode</td>
            <td>الرسم الإملائي بترميز يونيكود</td>
            <td>The Unicode of Uthmani script for each token</td>
        </tr>
        <tr>
            <td>12</td>
            <td>phonetic</td>
            <td>الترميز الصوتي للكلمات</td>
            <td>Phonetic encoding for each word</td>
        </tr>
    </tbody>
</table>

3. **Morphological Layer**: Focuses on the word-level analysis, detailing the morphological structure of each word. This includes the root, pattern, and grammatical attributes. The table below outlines the details.
   
<table>
    <thead>
        <tr>
            <th>No.</th>
            <th>Column</th>
            <th>Description-Arabic</th>
            <th>Description-English</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Tid</td>
            <td>عداد تسلسلي لصفوف الجدول</td>
            <td>Sequence counter for table rows</td>
        </tr>
        <tr>
            <td>2</td>
            <td>sentence_id</td>
            <td>عداد تسلسلي لجمل الكوربس</td>
            <td>Serial counter for sentences in the corpus/treebank</td>
        </tr>
        <tr>
            <td>3</td>
            <td>sentence_word</td>
            <td>عداد تسلسلي لكلمات كل جملة من جمل الكوربس</td>
            <td>Serial counter for the word in each sentence within the corpus/treebank</td>
        </tr>
        <tr>
            <td>4</td>
            <td>token_id</td>
            <td>عداد تسلسلي لتوكن كل كلمة من كلمات كل جملة من جمل الكوربس</td>
            <td>Serial counter for tokens of each word for each sentence in the corpus/treebank</td>
        </tr>
        <tr>
            <td>5</td>
            <td>location</td>
            <td>ترميز لموقع كل توكن وفق الترميز القرآني (التوكن: الكلمة: الآية: السورة)</td>
            <td>Code for encoding each token location in Quran (token: word: verse: surah/chapter)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>chapter_id</td>
            <td>عداد تسلسلي لسور القران الكريم المتكون من 114 سورة</td>
            <td>Serial counter for the surah/chapter in Quran, which consists of 114 surahs/chapters</td>
        </tr>
        <tr>
            <td>7</td>
            <td>verse_id</td>
            <td>عداد تسلسلي لآيات كل سورة في القران الكريم</td>
            <td>Serial counter of the verses in each surah/chapter in Quran</td>
        </tr>
        <tr>
            <td>8</td>
            <td>word_id</td>
            <td>عداد تسلسلي لكلمات كل آية في القران الكريم</td>
            <td>Serial counter of each word in each verse in Quran</td>
        </tr>
        <tr>
            <td>9</td>
            <td>tok_id</td>
            <td>عداد تسلسلي لتوكن كل كلمة في القران الكريم</td>
            <td>A serial counter for tokens in each word in Quran</td>
        </tr>
        <tr>
            <td>10</td>
            <td>imlaai_token</td>
            <td>الرسم الإملائي</td>
            <td>Imlaai script of the token</td>
        </tr>
        <tr>
            <td>11</td>
            <td>imlaai_unicode</td>
            <td>الرسم الإملائي بترميز يونيكود</td>
            <td>The Unicode of Uthmani script for each token</td>
        </tr>
        <tr>
            <td>12</td>
            <td>phonetic</td>
            <td>الترميز الصوتي للكلمات</td>
            <td>Phonetic encoding for each word</td>
        </tr>
    </tbody>
</table>

4. **Syntactic Layer**: This final layer provides the full syntactic analysis of each verse, presenting the relationship between words and their grammatical roles within the sentence. The table below outlines the syntactic information available.
   
<table>
    <thead>
        <tr>
            <th>No.</th>
            <th>Column</th>
            <th>Description-Arabic</th>
            <th>Description-English</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Tid</td>
            <td>عداد تسلسلي لصفوف الجدول</td>
            <td>Sequence counter for table rows</td>
        </tr>
        <tr>
            <td>2</td>
            <td>sentence_id</td>
            <td>عداد تسلسلي لجمل الكوربس</td>
            <td>Serial counter for sentences in the corpus/treebank</td>
        </tr>
        <tr>
            <td>3</td>
            <td>sentence_word</td>
            <td>عداد تسلسلي لكلمات كل جملة من جمل الكوربس</td>
            <td>Serial counter for the word in each sentence within the corpus/treebank</td>
        </tr>
        <tr>
            <td>4</td>
            <td>token_id</td>
            <td>عداد تسلسلي لتوكن كل كلمة من كلمات كل جملة من جمل الكوربس</td>
            <td>Serial counter for tokens of each word for each sentence in the corpus/treebank</td>
        </tr>
        <tr>
            <td>5</td>
            <td>location</td>
            <td>ترميز لموقع كل توكن وفق الترميز القرآني (التوكن: الكلمة: الآية: السورة)</td>
            <td>Code for encoding each token location in Quran (token: word: verse: surah/chapter)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>chapter_id</td>
            <td>عداد تسلسلي لسور القران الكريم المتكون من 114 سورة</td>
            <td>Serial counter for the surah/chapter in Quran, which consists of 114 surahs/chapters</td>
        </tr>
        <tr>
            <td>7</td>
            <td>verse_id</td>
            <td>عداد تسلسلي لآيات كل سورة في القران الكريم</td>
            <td>Serial counter of the verses in each surah/chapter in Quran</td>
        </tr>
        <tr>
            <td>8</td>
            <td>word_id</td>
            <td>عداد تسلسلي لكلمات كل آية في القران الكريم</td>
            <td>Serial counter of each word in each verse in Quran</td>
        </tr>
        <tr>
            <td>9</td>
            <td>tok_id</td>
            <td>عداد تسلسلي لتوكن كل كلمة في القران الكريم</td>
            <td>A serial counter for tokens in each word in Quran</td>
        </tr>
        <tr>
            <td>10</td>
            <td>imlaai_token</td>
            <td>الرسم الإملائي</td>
            <td>Imlaai script of the token</td>
        </tr>
        <tr>
            <td>11</td>
            <td>imlaai_unicode</td>
            <td>الرسم الإملائي بترميز يونيكود</td>
            <td>The Unicode of Uthmani script for each token</td>
        </tr>
        <tr>
            <td>12</td>
            <td>phonetic</td>
            <td>الترميز الصوتي للكلمات</td>
            <td>Phonetic encoding for each word</td>
        </tr>
    </tbody>
</table>

## Methodology

The Bayan treebank was developed through a structured, four-phase process, ensuring high-quality linguistic data:

### Phase 1: Data Selection
The initial data for Bayan was selected from the **Quranic Treebank**, a well-established treebank for Classical Arabic. This provided a solid linguistic foundation for the syntactic structures required for analyzing Arabic poetry.

### Phase 2: Fine-tuning the Linguistic Model
In this stage, the **Gemini** model was fine-tuned using selected data from the Quranic Treebank. This model serves as the core for syntactic analysis and linguistic feature extraction in Bayan.

### Phase 3: Building the Bayan Dataset
The Bayan treebank was constructed based on the refined model. This involved curating a selection of Arabic poems, followed by detailed annotation of the syntactic, morphological, and orthographic structures.

### Phase 4: Validation and Evaluation
The final step involved validating the accuracy of the Bayan dataset. This was done through automatic grammar-based algorithms that ensured the syntactic annotations were consistent with the linguistic rules of Arabic.

## Getting Started

### Prerequisites:
- **Python 3.8+** 
- **Pandas**, **NLTK**, and **spaCy** for linguistic processing and data manipulation.

To install the required dependencies:



## Data Structure:
- **Poems**: A collection of classical and modern Arabic poems with full syntactic annotation.
- **Syntax Trees**: Graphical representations stored as JSON files for easy parsing and manipulation.

## Usage

Bayan offers various functionalities, including:
- **Treebank Exploration**: Browse and explore the syntactic structure of poems.
- **Search Tool**: Use linguistic queries to search specific poems by syntactic features.
- **Custom Annotations**: Add or modify annotations to suit research needs.

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
