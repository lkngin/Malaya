.. code:: ipython3

    import pandas as pd
    import malaya

.. code:: ipython3

    df = pd.read_csv('tests/02032018.csv',sep=';')
    df = df.iloc[3:,1:]
    df.columns = ['text','label']
    corpus = df.text.tolist()

Load attention model
--------------------

We can use Transformer model to build topic modeling for corpus we have,
the power of attention!

.. code:: ipython3

    albert = malaya.transformer.load(model = 'albert')
    attention = malaya.topic_model.attention(corpus, n_topics = 10, vectorizer = albert)


.. parsed-literal::

    WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/albert/tokenization.py:240: The name tf.logging.info is deprecated. Please use tf.compat.v1.logging.info instead.
    
    INFO:tensorflow:loading sentence piece model
    WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/albert/modeling.py:116: The name tf.gfile.GFile is deprecated. Please use tf.io.gfile.GFile instead.
    
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/transformers/albert/__init__.py:62: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.
    
    WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/albert/modeling.py:194: The name tf.variable_scope is deprecated. Please use tf.compat.v1.variable_scope instead.
    
    WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/albert/modeling.py:507: The name tf.get_variable is deprecated. Please use tf.compat.v1.get_variable instead.
    
    WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/albert/modeling.py:588: The name tf.assert_less_equal is deprecated. Please use tf.compat.v1.assert_less_equal instead.
    
    WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/albert/modeling.py:1025: The name tf.AUTO_REUSE is deprecated. Please use tf.compat.v1.AUTO_REUSE instead.
    
    WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/albert/modeling.py:253: dense (from tensorflow.python.layers.core) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use keras.layers.Dense instead.
    WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/tensorflow_core/python/layers/core.py:187: Layer.apply (from tensorflow.python.keras.engine.base_layer) is deprecated and will be removed in a future version.
    Instructions for updating:
    Please use `layer.__call__` method instead.
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/transformers/sampling.py:26: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use tf.where in 2.0, which has the same broadcast rule as np.where
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/transformers/albert/__init__.py:118: multinomial (from tensorflow.python.ops.random_ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use `tf.random.categorical` instead.
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/transformers/albert/__init__.py:121: The name tf.InteractiveSession is deprecated. Please use tf.compat.v1.InteractiveSession instead.
    
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/transformers/albert/__init__.py:122: The name tf.global_variables_initializer is deprecated. Please use tf.compat.v1.global_variables_initializer instead.
    
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/transformers/albert/__init__.py:123: The name tf.get_collection is deprecated. Please use tf.compat.v1.get_collection instead.
    
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/transformers/albert/__init__.py:124: The name tf.GraphKeys is deprecated. Please use tf.compat.v1.GraphKeys instead.
    
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/transformers/albert/__init__.py:129: The name tf.train.Saver is deprecated. Please use tf.compat.v1.train.Saver instead.
    
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/transformers/albert/__init__.py:131: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.
    
    INFO:tensorflow:Restoring parameters from /Users/huseinzolkepli/Malaya/albert-model/base/albert-base/model.ckpt


Get topics
^^^^^^^^^^

.. code:: ipython3

    attention.top_topics(5, top_n = 10, return_df = True)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>topic 0</th>
          <th>topic 1</th>
          <th>topic 2</th>
          <th>topic 3</th>
          <th>topic 4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>kena</td>
          <td>bayar</td>
          <td>negara</td>
          <td>terima</td>
          <td>raja</td>
        </tr>
        <tr>
          <th>1</th>
          <td>rakyat</td>
          <td>nilai</td>
          <td>rakyat</td>
          <td>negara</td>
          <td>duit</td>
        </tr>
        <tr>
          <th>2</th>
          <td>menteri</td>
          <td>malaysia</td>
          <td>malaysia</td>
          <td>didik</td>
          <td>raja duit</td>
        </tr>
        <tr>
          <th>3</th>
          <td>raja</td>
          <td>negara</td>
          <td>kena</td>
          <td>isu</td>
          <td>daftar</td>
        </tr>
        <tr>
          <th>4</th>
          <td>selamat</td>
          <td>rana</td>
          <td>amanah</td>
          <td>didik latih</td>
          <td>terima</td>
        </tr>
        <tr>
          <th>5</th>
          <td>laku</td>
          <td>nyata</td>
          <td>arah</td>
          <td>tani didik</td>
          <td>rana</td>
        </tr>
        <tr>
          <th>6</th>
          <td>negara</td>
          <td>undi</td>
          <td>parti</td>
          <td>rakyat</td>
          <td>mahukan</td>
        </tr>
        <tr>
          <th>7</th>
          <td>perdana</td>
          <td>tulis nyata</td>
          <td>terima</td>
          <td>tangan isu</td>
          <td>lihat</td>
        </tr>
        <tr>
          <th>8</th>
          <td>hutang</td>
          <td>tulis</td>
          <td>kembang</td>
          <td>capai</td>
          <td>pecat</td>
        </tr>
        <tr>
          <th>9</th>
          <td>urus</td>
          <td>jaga</td>
          <td>raja</td>
          <td>bangun</td>
          <td>parti</td>
        </tr>
      </tbody>
    </table>
    </div>



Get topics as string
^^^^^^^^^^^^^^^^^^^^

.. code:: ipython3

    attention.get_topics(10)




.. parsed-literal::

    [(0, 'kena rakyat menteri raja selamat laku negara perdana hutang urus'),
     (1, 'bayar nilai malaysia negara rana nyata undi tulis nyata tulis jaga'),
     (2, 'negara rakyat malaysia kena amanah arah parti terima kembang raja'),
     (3,
      'terima negara didik isu didik latih tani didik rakyat tangan isu capai bangun'),
     (4, 'raja duit raja duit daftar terima rana mahukan lihat pecat parti'),
     (5,
      'menteri malaysia masyarakat kena syarikat statistik wang parti raja rakyat'),
     (6, 'rana parti pinggir rakyat raja pasar gembira harga nyata pelabur'),
     (7, 'umno putus wujud jalan malaysia hutang gaji wang status berita'),
     (8, 'rakyat undi selesai beli putus pilih pengerusi jual beli daftar pucuk'),
     (9,
      'lembaga lancar jalan lancar rana rendah rujuk jalan rujuk lembaga kerja babit kerja')]



Train LDA2Vec model
-------------------

.. code:: ipython3

    lda2vec = malaya.topic_model.lda2vec(corpus, 10, vectorizer = 'skip-gram', skip = 4)


.. parsed-literal::

    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/model/lda2vec.py:44: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.
    
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/model/lda2vec.py:47: The name tf.truncated_normal is deprecated. Please use tf.random.truncated_normal instead.
    
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/model/lda2vec.py:55: The name tf.random_normal is deprecated. Please use tf.random.normal instead.
    
    WARNING:tensorflow:
    The TensorFlow contrib module will not be included in TensorFlow 2.0.
    For more information, please see:
      * https://github.com/tensorflow/community/blob/master/rfcs/20180907-contrib-sunset.md
      * https://github.com/tensorflow/addons
      * https://github.com/tensorflow/io (for I/O related ops)
    If you depend on functionality not listed there, please file an issue.
    
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/model/lda2vec.py:104: The name tf.train.get_global_step is deprecated. Please use tf.compat.v1.train.get_global_step instead.
    
    WARNING:tensorflow:From /Users/huseinzolkepli/Documents/Malaya/malaya/model/lda2vec.py:117: The name tf.assign is deprecated. Please use tf.compat.v1.assign instead.
    


.. parsed-literal::

    minibatch loop: 100%|██████████| 287/287 [00:00<00:00, 332.79it/s, cost=-7.32e+3, epoch=1]
    minibatch loop: 100%|██████████| 287/287 [00:00<00:00, 396.96it/s, cost=-7.92e+3, epoch=2]
    minibatch loop: 100%|██████████| 287/287 [00:00<00:00, 399.53it/s, cost=-8.56e+3, epoch=3]
    minibatch loop: 100%|██████████| 287/287 [00:00<00:00, 392.99it/s, cost=-9.2e+3, epoch=4] 
    minibatch loop: 100%|██████████| 287/287 [00:00<00:00, 409.40it/s, cost=-9.86e+3, epoch=5]
    minibatch loop: 100%|██████████| 287/287 [00:00<00:00, 394.66it/s, cost=-1.05e+4, epoch=6]
    minibatch loop: 100%|██████████| 287/287 [00:00<00:00, 392.33it/s, cost=-1.12e+4, epoch=7]
    minibatch loop: 100%|██████████| 287/287 [00:00<00:00, 355.67it/s, cost=-1.19e+4, epoch=8]
    minibatch loop: 100%|██████████| 287/287 [00:00<00:00, 398.37it/s, cost=-1.26e+4, epoch=9]
    minibatch loop: 100%|██████████| 287/287 [00:00<00:00, 378.69it/s, cost=-1.33e+4, epoch=10]


Get topics
^^^^^^^^^^

You able to set to return as Pandas Dataframe or not by using
``return_df`` parameter

.. code:: ipython3

    lda2vec.top_topics(5, top_n = 10, return_df = True)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>topic 0</th>
          <th>topic 1</th>
          <th>topic 2</th>
          <th>topic 3</th>
          <th>topic 4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>alam ekonomi sosial</td>
          <td>tuntut</td>
          <td>bangun rangka program</td>
          <td>insya</td>
          <td>lihat projek</td>
        </tr>
        <tr>
          <th>1</th>
          <td>selatan selatan</td>
          <td>negara maju bidang</td>
          <td>serius pimpin</td>
          <td>amanah</td>
          <td>amanah</td>
        </tr>
        <tr>
          <th>2</th>
          <td>putus</td>
          <td>pulang</td>
          <td>negara selatan</td>
          <td>malaysia peran</td>
          <td>simpul</td>
        </tr>
        <tr>
          <th>3</th>
          <td>malaysia main peran</td>
          <td>komprehensif</td>
          <td>wajar</td>
          <td>cemar</td>
          <td>bangun program kerjasama</td>
        </tr>
        <tr>
          <th>4</th>
          <td>gagal</td>
          <td>kerjasama malaysia</td>
          <td>ahli</td>
          <td>manfaat</td>
          <td>guru</td>
        </tr>
        <tr>
          <th>5</th>
          <td>bertanggungjawab</td>
          <td>bank negara</td>
          <td>peran</td>
          <td>bahan uji</td>
          <td>jatuh</td>
        </tr>
        <tr>
          <th>6</th>
          <td>jejas</td>
          <td>bimbang</td>
          <td>manfaat</td>
          <td>malaysia sedia malaysia</td>
          <td>pulang</td>
        </tr>
        <tr>
          <th>7</th>
          <td>ancang ekonomi</td>
          <td>malaysia sedia malaysia</td>
          <td>bidang proses ajar</td>
          <td>serius</td>
          <td>sewa</td>
        </tr>
        <tr>
          <th>8</th>
          <td>syarikat terbang</td>
          <td>daftar ph</td>
          <td>keluarga</td>
          <td>pulang</td>
          <td>negara maju bidang</td>
        </tr>
        <tr>
          <th>9</th>
          <td>program kerjasama malaysia</td>
          <td>bangun negara selatan</td>
          <td>berbeza</td>
          <td>alam bangun negara</td>
          <td>manfaat</td>
        </tr>
      </tbody>
    </table>
    </div>



Important sentences based on topics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: ipython3

    lda2vec.get_sentences(5)




.. parsed-literal::

    ['konon fokus pilih raya',
     'sokong',
     'nampak nama',
     'masuk saiful bentuk gelombang pakat ph rana nali intelek melayu bakat',
     'negara berita palsu raja autoritarian melenyapka tuduh langgar hak asasi manusia']



Get topics as string
^^^^^^^^^^^^^^^^^^^^

.. code:: ipython3

    lda2vec.get_topics(10)




.. parsed-literal::

    [(0,
      'alam ekonomi sosial selatan selatan putus malaysia main peran gagal bertanggungjawab jejas ancang ekonomi syarikat terbang program kerjasama malaysia'),
     (1,
      'tuntut negara maju bidang pulang komprehensif kerjasama malaysia bank negara bimbang malaysia sedia malaysia daftar ph bangun negara selatan'),
     (2,
      'bangun rangka program serius pimpin negara selatan wajar ahli peran manfaat bidang proses ajar keluarga berbeza'),
     (3,
      'insya amanah malaysia peran cemar manfaat bahan uji malaysia sedia malaysia serius pulang alam bangun negara'),
     (4,
      'lihat projek amanah simpul bangun program kerjasama guru jatuh pulang sewa negara maju bidang manfaat'),
     (5,
      'kongsi alam mahir sivil doj serah kalang sumbang ajar ajar aabar bvi tanding bon teras'),
     (6,
      'amanah bangun arus perdana simpul babit parti fasal lembaga fasal umno terima kasih didik ajar air bersih kandung tuntut sivil'),
     (7,
      'impak bekal bersih kampung sosial negara rangka amanah bahan kaji air bersih tinggal kerja kerja bukti'),
     (8,
      'kongsi alam negara arus malaysia kongsi bangun kongsi bangun negara kerja kerja bangun program kerjasama huni ekonomi dagang tani dunia nik aziz'),
     (9,
      'impak bank negara bidang didik bincang kampung kumpul didik teknikal industri bangun arus perdana sewa bekal bersih')]



Visualize topics
^^^^^^^^^^^^^^^^

.. code:: ipython3

    lda2vec.visualize_topics(notebook_mode = True)


.. parsed-literal::

    /usr/local/lib/python3.7/site-packages/past/types/oldstr.py:5: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working
      from collections import Iterable




.. raw:: html

    
    <link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.css">
    
    
    <div id="ldavis_el8715855864430882865459121"></div>
    <script type="text/javascript">
    
    var ldavis_el8715855864430882865459121_data = {"mdsDat": {"x": [6.483514472896526e-05, -0.0001150471639046365, -0.00011037044763073875, 3.811080627912134e-05, 0.00010057280621343401, 5.3437703795988234e-05, 0.000315936174408859, -1.3465990162499241e-05, -4.6219695578503364e-05, -0.0002877893381499904], "y": [-0.00011259035192999638, 0.00018473907232376675, 7.078710482835243e-06, -6.731990274030316e-05, -5.1882115236987564e-05, 3.792682046237447e-05, 7.897351922498822e-05, -0.00015016830551351312, 0.00012086490292567176, -4.762234999883646e-05], "topics": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "cluster": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "Freq": [12.518013954162598, 11.695584297180176, 11.271976470947266, 10.673222541809082, 10.573539733886719, 10.49451732635498, 10.154807090759277, 8.337812423706055, 8.140984535217285, 6.139541149139404]}, "tinfo": {"Category": ["Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10"], "Freq": [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 0.4483184218406677, 0.45091238617897034, 0.4449779689311981, 0.4249047040939331, 0.4417136311531067, 0.42892035841941833, 0.43617793917655945, 0.42319419980049133, 0.44686654210090637, 0.4548763930797577, 0.44881322979927063, 0.43956005573272705, 0.43102556467056274, 0.43754106760025024, 0.436352014541626, 0.4238591492176056, 0.43737179040908813, 0.43729209899902344, 0.4420364201068878, 0.42758840322494507, 0.4385511875152588, 0.4375484585762024, 0.4411526024341583, 0.4219554364681244, 0.4441835582256317, 0.4338180422782898, 0.44280004501342773, 0.4336056411266327, 0.4207274913787842, 0.42066556215286255, 0.4473658800125122, 0.4420579671859741, 0.45029112696647644, 0.43888089060783386, 0.4447333514690399, 0.43905824422836304, 0.4423378109931946, 0.4491197466850281, 0.4436946511268616, 0.45088908076286316, 0.44257885217666626, 0.44273102283477783, 0.44439998269081116, 0.44133374094963074, 0.44314080476760864, 0.4413740932941437, 0.441557914018631, 0.4404744803905487, 0.4411168396472931, 0.4394310414791107, 0.44878020882606506, 0.4183104336261749, 0.41493844985961914, 0.42476820945739746, 0.42841440439224243, 0.4479111135005951, 0.4245542883872986, 0.42229941487312317, 0.431435763835907, 0.4316515326499939, 0.4356604516506195, 0.4136658310890198, 0.43227341771125793, 0.41470035910606384, 0.4346168339252472, 0.43241962790489197, 0.42799973487854004, 0.419418066740036, 0.41436338424682617, 0.4186938405036926, 0.4135804772377014, 0.4209917485713959, 0.4280751943588257, 0.41422292590141296, 0.41126927733421326, 0.40546077489852905, 0.424062579870224, 0.41464272141456604, 0.41429510712623596, 0.418885201215744, 0.41179805994033813, 0.42159321904182434, 0.42631345987319946, 0.42371824383735657, 0.4255940616130829, 0.4222524166107178, 0.42231354117393494, 0.42650464177131653, 0.41952213644981384, 0.4205763638019562, 0.4202665090560913, 0.4194108247756958, 0.3947773873806, 0.4059560298919678, 0.387095183134079, 0.4013718068599701, 0.3859240412712097, 0.4030860960483551, 0.388759046792984, 0.3968104422092438, 0.3843442499637604, 0.3932282030582428, 0.3827522397041321, 0.3897610604763031, 0.3930022120475769, 0.38709643483161926, 0.39233458042144775, 0.40931305289268494, 0.3889217674732208, 0.39977145195007324, 0.3954988420009613, 0.3967753052711487, 0.3815569579601288, 0.4112938642501831, 0.3913743793964386, 0.38751089572906494, 0.3879392445087433, 0.3845720887184143, 0.4015105962753296, 0.3849365711212158, 0.40672463178634644, 0.380980908870697, 0.4025207757949829, 0.4023970365524292, 0.39527496695518494, 0.39418673515319824, 0.3928714692592621, 0.39197027683258057, 0.4006323516368866, 0.40238314867019653, 0.40063363313674927, 0.39435291290283203, 0.40093380212783813, 0.3975542187690735, 0.39587631821632385, 0.39834272861480713, 0.39599183201789856, 0.39714059233665466, 0.39473867416381836, 0.3972645103931427, 0.3968973457813263, 0.3957104980945587, 0.39778825640678406, 0.3979978859424591, 0.3952842950820923, 0.39504653215408325, 0.3888902962207794, 0.38655319809913635, 0.3775355815887451, 0.36791619658470154, 0.3845597505569458, 0.3807012438774109, 0.37528014183044434, 0.38345015048980713, 0.36812224984169006, 0.3556915819644928, 0.3735697865486145, 0.38264548778533936, 0.3779388666152954, 0.37100884318351746, 0.38134765625, 0.3682596683502197, 0.3666820228099823, 0.37360823154449463, 0.37988632917404175, 0.364543616771698, 0.3723181188106537, 0.3727783262729645, 0.3737778961658478, 0.38253360986709595, 0.3630309998989105, 0.38120147585868835, 0.38005053997039795, 0.35436108708381653, 0.36643046140670776, 0.36826643347740173, 0.3749404847621918, 0.3806436061859131, 0.37417808175086975, 0.37492507696151733, 0.3720795214176178, 0.37149131298065186, 0.372759610414505, 0.3795669674873352, 0.378429651260376, 0.3781795799732208, 0.3766816258430481, 0.3775702118873596, 0.37492987513542175, 0.37429121136665344, 0.3740726113319397, 0.37292972207069397, 0.3764868378639221, 0.3659801781177521, 0.3682958781719208, 0.3582598865032196, 0.371551513671875, 0.36236098408699036, 0.36701712012290955, 0.3540184795856476, 0.35419291257858276, 0.3636433780193329, 0.36991366744041443, 0.3624860942363739, 0.36378222703933716, 0.351548433303833, 0.3655305802822113, 0.35214492678642273, 0.3658164441585541, 0.3588904142379761, 0.35594114661216736, 0.36638548970222473, 0.3586404323577881, 0.34688758850097656, 0.3599125146865845, 0.3621331751346588, 0.3616390824317932, 0.36111360788345337, 0.3559286296367645, 0.3619301915168762, 0.3622477054595947, 0.3585052192211151, 0.36752834916114807, 0.3655627369880676, 0.36606061458587646, 0.3642421066761017, 0.3668428957462311, 0.36633989214897156, 0.3675457835197449, 0.37000972032546997, 0.3641250431537628, 0.37183886766433716, 0.3633151054382324, 0.3716331422328949, 0.3659752607345581, 0.37132614850997925, 0.36793574690818787, 0.3651307225227356, 0.3670344352722168, 0.3658939599990845, 0.3651294410228729, 0.36490869522094727, 0.36529865860939026, 0.3653445541858673, 0.3901611268520355, 0.35881656408309937, 0.3746228516101837, 0.3651438057422638, 0.37024953961372375, 0.36533740162849426, 0.3718886077404022, 0.3632604777812958, 0.3696257174015045, 0.3539030849933624, 0.36077460646629333, 0.3753367066383362, 0.3664596378803253, 0.3626224398612976, 0.3756681978702545, 0.35896235704421997, 0.36539673805236816, 0.3776686489582062, 0.3702485263347626, 0.35501334071159363, 0.3602806031703949, 0.3548646569252014, 0.3635658621788025, 0.3567214608192444, 0.3637971580028534, 0.35449472069740295, 0.365149587392807, 0.3727000653743744, 0.363542765378952, 0.3746584355831146, 0.38032445311546326, 0.3671712875366211, 0.3752954602241516, 0.36946532130241394, 0.37827420234680176, 0.38159799575805664, 0.3683546483516693, 0.3674977123737335, 0.37184277176856995, 0.37190020084381104, 0.36606666445732117, 0.37153154611587524, 0.36709752678871155, 0.3717469573020935, 0.3680076003074646, 0.3669460117816925, 0.3671168386936188, 0.36615896224975586, 0.3662518262863159, 0.3756987452507019, 0.35564252734184265, 0.3756089210510254, 0.35465914011001587, 0.3507552146911621, 0.3666177988052368, 0.34747859835624695, 0.3556228280067444, 0.36342522501945496, 0.3620586395263672, 0.3497113585472107, 0.3548312783241272, 0.36150601506233215, 0.36386990547180176, 0.3435538709163666, 0.3626278340816498, 0.36007797718048096, 0.3645382821559906, 0.35755330324172974, 0.35197293758392334, 0.35461124777793884, 0.35456109046936035, 0.3493102788925171, 0.3512084484100342, 0.3548852801322937, 0.3422287404537201, 0.3594939708709717, 0.35948851704597473, 0.35836538672447205, 0.3492424190044403, 0.35923877358436584, 0.3633655905723572, 0.3614063858985901, 0.35662612318992615, 0.357011616230011, 0.3586970567703247, 0.3565223217010498, 0.35397693514823914, 0.3561244606971741, 0.35723596811294556, 0.3556826710700989, 0.3551066517829895, 0.3552699089050293, 0.35491207242012024, 0.2905629575252533, 0.28321805596351624, 0.29463785886764526, 0.2850140631198883, 0.2891518175601959, 0.2859303951263428, 0.29189616441726685, 0.2884277403354645, 0.2905288636684418, 0.27979913353919983, 0.29184913635253906, 0.2822570502758026, 0.2828582525253296, 0.2843858599662781, 0.284686803817749, 0.2868242561817169, 0.2895455062389374, 0.29099133610725403, 0.2833084166049957, 0.28076255321502686, 0.292509526014328, 0.2776893973350525, 0.2844877541065216, 0.29227182269096375, 0.2844034731388092, 0.28800055384635925, 0.28961849212646484, 0.27444544434547424, 0.28333115577697754, 0.28615090250968933, 0.28796321153640747, 0.2947821021080017, 0.29535484313964844, 0.29431530833244324, 0.289837509393692, 0.2926015555858612, 0.29140812158584595, 0.2902792692184448, 0.2904875576496124, 0.29271167516708374, 0.29074448347091675, 0.2894386053085327, 0.2908506393432617, 0.29192283749580383, 0.29069432616233826, 0.28893741965293884, 0.29097065329551697, 0.2895362079143524, 0.2890383005142212, 0.2892872989177704, 0.2892225384712219, 0.31294122338294983, 0.30035915970802307, 0.3044760227203369, 0.2999963164329529, 0.29408928751945496, 0.2957113981246948, 0.29133179783821106, 0.29243120551109314, 0.28849658370018005, 0.2866370379924774, 0.28867530822753906, 0.28455063700675964, 0.29333487153053284, 0.2934843897819519, 0.28934940695762634, 0.2827688753604889, 0.2906288504600525, 0.2886028289794922, 0.2834709882736206, 0.303786963224411, 0.2892465889453888, 0.2970452308654785, 0.2855512499809265, 0.2842805087566376, 0.28304755687713623, 0.2879765033721924, 0.2897970378398895, 0.2970134913921356, 0.29323098063468933, 0.28561416268348694, 0.289233535528183, 0.2930411696434021, 0.2925509512424469, 0.2914750277996063, 0.28763729333877563, 0.295400470495224, 0.2944008708000183, 0.2899671792984009, 0.29009687900543213, 0.2902083694934845, 0.2892248034477234, 0.28927087783813477, 0.2891504764556885, 0.22504939138889313, 0.23131303489208221, 0.22919714450836182, 0.22495685517787933, 0.2240106463432312, 0.22094665467739105, 0.226478710770607, 0.22618304193019867, 0.2276868224143982, 0.22301556169986725, 0.22479450702667236, 0.21742960810661316, 0.23021431267261505, 0.224932461977005, 0.2220979481935501, 0.22607503831386566, 0.23120830953121185, 0.23160679638385773, 0.22137023508548737, 0.22873955965042114, 0.21948309242725372, 0.21816709637641907, 0.22334517538547516, 0.220000222325325, 0.21182933449745178, 0.224112406373024, 0.21854348480701447, 0.21905864775180817, 0.22245414555072784, 0.21063674986362457, 0.22075416147708893, 0.22613047063350677, 0.2223561406135559, 0.22464996576309204, 0.2226579338312149, 0.22824405133724213, 0.22548983991146088, 0.224358931183815, 0.22563767433166504, 0.22197100520133972], "Term": ["bahan kaji", "tinggal", "kerja kerja", "individu", "maklum", "bukti", "mtcp", "alam bangun ekonomi", "fasal", "air bersih", "bangun rangka kerjasama", "kampung", "bekal bersih", "sewa", "negara bangun rangka", "faham", "sosial negara rangka", "peringkat", "tutup", "aspirasi", "masuk", "khidmat", "sosial negara bangun", "tuduh", "sasar", "lihat projek", "air", "urus niaga jho", "tingkat bidang", "sosial bangun", "peran", "negara selatan", "berbeza", "pru", "ahli parti", "dengar", "politik arah", "jual beli", "keluarga", "bangun rangka program", "wajar", "tingkat bidang didik", "pelan", "melayu", "urus jho low", "masyarakat asli", "jabat perdana", "uji kaji", "negara bangun rangka", "bvi", "bangun negara negara", "negara bangun", "resolusi", "wang tani didik", "tumbuh", "bidang didik proses", "pindah kampung", "rupa", "kongsi", "nampak", "bidang proses ajar", "laku tingkat", "serius pimpin", "tuju", "ekonomi sosial negara", "luas", "kampung", "ahli", "didik proses", "manfaat", "teras", "nik aziz", "bentuk", "ancang wang", "jatuh", "didik ajar", "terima kasih", "menteri jabat perdana", "amanah", "tanding", "bangun arus perdana", "tuntut sivil doj", "dagang didik", "terjemah", "kandung tuntut sivil", "amanah", "ekonomi sosial", "isu politik", "fasal umno", "parti fasal lembaga", "simpul", "seri razak", "didik ajar", "tubuh", "babit", "terima kasih", "teknikal diplomasi", "bekal air", "majlis", "janji", "harga", "serah", "air bersih", "main peran", "suasana", "benda", "global", "latih", "malaysia kongsi alam", "peribadi", "musnah", "tingkat maju bidang", "menteri jabat perdana", "sosial bangun rangka", "bekal bersih", "guru", "sosial negara rangka", "manfaat", "tn", "bank negara", "bidang didik", "negara maju bidang", "kawasan bandar", "bincang", "menteri jabat", "kumpul", "diplomasi", "kampung", "kembang", "maklum", "bangun sosial negara", "malaysia sedia", "gabung", "baca", "nila", "mtcp sedia malaysia", "dagang tani", "bank negara", "teknikal malaysia", "lancar", "didik latih industri", "bangun negara", "tingkat maju", "impak", "tuntut sivil", "bangkang", "pas parti", "fasal", "sewa", "kongsi alam ekonomi", "bidang didik", "raja maju bidang", "maju didik proses", "didik teknikal industri", "bukti", "hakim", "nik", "teknikal malaysia mtcp", "sosial negara rangka", "bangun arus perdana", "simpul", "mtcp", "bekal bersih", "teknikal diplomasi", "maju ancang ekonomi", "selatan", "bimbang laku", "bidang ekonomi", "sasar", "terima kasih", "aabar", "atur", "manfaat", "amanah", "tanding", "fungsi", "kongsi alam negara", "arus", "arab", "jalan lancar", "malaysia kongsi bangun", "aktiviti", "bantu negara negara", "kongsi bangun negara", "kerjasama teknikal mtcp", "malaysia", "ppsmi", "ekonomi dagang tani", "faham", "kaya", "bangun program kerjasama", "sidang", "kapal", "jual syarikat", "laku raja maju", "rangka program", "bangun rangka", "pakat", "suasana", "kerja kerja", "razak", "huni", "dunia", "alat", "belia", "program", "kait mdb", "nik aziz", "didik ajar ajar", "mesyuarat", "aabar bvi", "perdana seri najib", "wajar", "lihat projek", "malaysia peran", "jatuh", "air bersih", "bekal bersih", "bahasa inggeris bahasa", "rampas", "global", "sedia kongsi", "insya", "negara maju ancang", "serius", "daftar", "cemar", "politik", "alam bangun negara", "doj", "masyarakat", "bahasa", "bahan uji", "malaysia mtcp", "kongsi bangun ekonomi", "demokrasi", "lapor", "nhrap", "hati", "berita palsu", "media", "putus umno", "galak", "bahan", "prestasi", "dagang", "bantu negara negara", "laku jemaah", "sokong", "sedia kongsi bangun", "latih industri diplomasi", "asasi manusia", "sedia alam bangun", "ekonomi", "strategi", "trx", "keras", "laku tingkat maju", "sukan", "malaysia sedia malaysia", "bersih", "malaysia peran", "hak asasi", "manfaat", "alam mahir bangun", "amanah", "pulang", "urus niaga jho", "babit", "fungsi", "bidang ekonomi", "malaysia mtcp sedia", "lihat projek", "negara maju bidang", "tuntut", "negara bangun program", "kerjasama malaysia", "bahagian", "hati", "lupa", "mtcp sedia", "asasi manusia", "sedia malaysia alam", "buah", "undang", "daftar ph", "tangguh pilih", "gembira lihat projek", "bimbang", "teknikal industri diplomasi", "menteri kena", "komprehensif", "ekonomi wang dagang", "seri najib", "bawa", "wang dagang", "teknikal mtcp sedia", "kempen", "kerjasama", "menteri seri razak", "bahan uji", "urus niaga jho", "arab saudi", "bangun negara selatan", "pulang", "luas", "malaysia sedia malaysia", "tangguh parti", "bank negara", "negara maju bidang", "bangun negara", "dagang tani latih", "atur", "aabar", "malaysia kongsi alam", "bangun arus perdana", "malaysia main kongsi", "manfaat", "selatan", "tangguh pilih parti", "amanah", "serah", "menteri seri", "selatan selatan", "jppm", "alam ekonomi sosial", "mac", "main peran alam", "putus", "maju bidang ancang", "mahir bangun kawasan", "bertanggungjawab", "syarikat terbang", "kali", "padang", "ancang ekonomi", "program kerjasama malaysia", "teruk", "jejas", "gembira lihat projek", "gagal", "kongsi alam", "perdana", "malaysia alam", "pelbagai", "menteri najib", "urus", "kandung tuntut", "perdana menteri kena", "melayu cina", "aset", "bekal", "kongsi mahir bangun", "anjur", "malaysia main peran", "dagang tani latih", "bilion", "musuh", "lihat", "sedia alam bangun", "pindah baharu", "program teknikal malaysia", "simpul", "undi", "kongsi bangun negara", "masuk rumah", "guru", "ph rana", "khusus", "sivil doj", "dengar", "alam negara negara", "bvi", "bon", "negara maju", "lantan", "daftar", "tuduh", "peran kongsi mahir", "gembira", "razak", "buka", "ekonomi dagang", "teknikal mtcp sedia", "tingkat", "raja tingkat maju", "nyata laku", "ajar ajar", "jho", "antarabangsa", "aabar bvi", "peringkat", "ulang kali", "bangun program", "murah", "tingkat maju didik", "individu", "bangun negara negara", "serah", "kongsi alam mahir", "kalang", "aspirasi", "urus niaga jho", "cabar", "april", "sosial bangun", "sumbang", "giat hidup", "didik ajar ajar", "dunia", "tanding", "teras", "kongsi mahir", "didik ajar", "lancar", "laku raja tingkat", "bidang ekonomi", "terima kasih", "lihat projek", "bangun program kerjasama", "simpul", "guru", "alam mahir bangun", "sewa", "menteri perdana menteri", "langgar", "titik", "aktiviti", "terjemah", "putrajaya", "alam bangun sosial", "kerja kerja", "ekonomi sosial", "negara rangka program", "mtcp", "ikan", "tentera", "amanah", "tadbir negara", "pulang", "mudah", "lantik", "rangka", "airasia", "lembaga umno", "jatuh", "teknikal diplomasi", "perdana seri najib", "gera", "malaysia mtcp sedia", "parti fasal lembaga", "malaysia sedia malaysia", "mesyuarat", "manfaat", "negara maju bidang", "maju didik proses", "sosial bangun rangka", "bekal bersih", "aabar", "malaysia peran", "fungsi", "fasal", "kampung", "bahan kaji", "negara bangun rangka", "maklum", "individu", "bukti", "alam bangun ekonomi", "tinggal", "masuk", "bangun rangka kerjasama", "peringkat", "sosial negara rangka", "mtcp", "wang mdb", "kerja kerja", "bekal bersih", "impak", "khidmat", "air bersih", "nila", "tutup", "sasar", "takut", "tadbir", "sewa", "faham", "aspirasi", "sedia kongsi alam", "menteri jabat", "air", "bidang didik", "teras", "hadap kumpul", "bangun negara selatan", "amanah", "bangun arus perdana", "fungsi", "manfaat", "tani didik"], "Total": [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.2776684761047363, 3.3081462383270264, 3.2731006145477295, 3.1279349327087402, 3.2756524085998535, 3.188227891921997, 3.2456271648406982, 3.149209976196289, 3.3271737098693848, 3.3879497051239014, 3.343585968017578, 3.2822375297546387, 3.218719244003296, 3.2673873901367188, 3.2605016231536865, 3.169394016265869, 3.2749547958374023, 3.275560140609741, 3.312737464904785, 3.20672345161438, 3.2895758152008057, 3.2824816703796387, 3.313765525817871, 3.170935869216919, 3.3386006355285645, 3.269252061843872, 3.3391189575195312, 3.2733662128448486, 3.1763808727264404, 3.1763617992401123, 3.3781533241271973, 3.3408851623535156, 3.412785291671753, 3.317317247390747, 3.3797850608825684, 3.325751781463623, 3.3631746768951416, 3.4446020126342773, 3.3879098892211914, 3.5088143348693848, 3.38667631149292, 3.3955845832824707, 3.4293835163116455, 3.3699207305908203, 3.4553682804107666, 3.43245792388916, 3.4436166286468506, 3.4564783573150635, 3.5215349197387695, 3.417299747467041, 3.4692070484161377, 3.264348030090332, 3.2455697059631348, 3.3271095752716064, 3.361454963684082, 3.5215349197387695, 3.3410277366638184, 3.334707021713257, 3.40688157081604, 3.4106805324554443, 3.4489128589630127, 3.284301280975342, 3.43245792388916, 3.2975943088531494, 3.456930637359619, 3.4436166286468506, 3.4117379188537598, 3.3453989028930664, 3.3060460090637207, 3.3427116870880127, 3.3073670864105225, 3.3718490600585938, 3.4318954944610596, 3.3297512531280518, 3.307919502258301, 3.2622859477996826, 3.412187099456787, 3.3369781970977783, 3.3355064392089844, 3.373629331588745, 3.3197336196899414, 3.410727024078369, 3.4564783573150635, 3.432797431945801, 3.4633429050445557, 3.430643320083618, 3.4357054233551025, 3.5088143348693848, 3.4138565063476562, 3.4481263160705566, 3.4479217529296875, 3.489077091217041, 3.247781753540039, 3.344383955001831, 3.204206943511963, 3.338909387588501, 3.2190158367156982, 3.3631746768951416, 3.244447708129883, 3.3116798400878906, 3.220942974090576, 3.295743465423584, 3.2114882469177246, 3.2704148292541504, 3.3060483932495117, 3.2576730251312256, 3.3021836280822754, 3.4481263160705566, 3.2803447246551514, 3.372685194015503, 3.337338447570801, 3.3484909534454346, 3.220550060272217, 3.472402811050415, 3.304530143737793, 3.2769551277160645, 3.2820563316345215, 3.2562880516052246, 3.4005990028381348, 3.2604572772979736, 3.4479217529296875, 3.2311484813690186, 3.413961887359619, 3.4153358936309814, 3.3558878898620605, 3.3472001552581787, 3.3344459533691406, 3.3283939361572266, 3.4357054233551025, 3.4692070484161377, 3.4489128589630127, 3.3632073402404785, 3.4633429050445557, 3.4117379188537598, 3.3888254165649414, 3.435950756072998, 3.4019834995269775, 3.4281058311462402, 3.3750016689300537, 3.4436166286468506, 3.436028003692627, 3.4057228565216064, 3.5088143348693848, 3.5215349197387695, 3.417299747467041, 3.452221155166626, 3.25260066986084, 3.2799625396728516, 3.2065773010253906, 3.172272205352783, 3.332273244857788, 3.3026225566864014, 3.2592084407806396, 3.341641426086426, 3.2109317779541016, 3.109133243560791, 3.2667346000671387, 3.3481485843658447, 3.316803216934204, 3.2709879875183105, 3.3654510974884033, 3.2502450942993164, 3.236807107925415, 3.298091411590576, 3.356015682220459, 3.2210423946380615, 3.2918152809143066, 3.2964086532592773, 3.307919502258301, 3.386089563369751, 3.2212839126586914, 3.3840723037719727, 3.3767647743225098, 3.1494274139404297, 3.258166551589966, 3.2748117446899414, 3.341310501098633, 3.3955845832824707, 3.341287136077881, 3.351895332336426, 3.3311378955841064, 3.3232827186584473, 3.343585968017578, 3.461782932281494, 3.448855400085449, 3.4553682804107666, 3.4318954944610596, 3.4633429050445557, 3.394737720489502, 3.396038055419922, 3.412187099456787, 3.3526086807250977, 3.291370391845703, 3.212231397628784, 3.2454841136932373, 3.1655654907226562, 3.2984180450439453, 3.2208104133605957, 3.265430212020874, 3.152553081512451, 3.1543781757354736, 3.247116804122925, 3.303354024887085, 3.237305164337158, 3.2506167888641357, 3.1501541137695312, 3.2783701419830322, 3.1613447666168213, 3.2848448753356934, 3.225677967071533, 3.2004458904266357, 3.29650616645813, 3.2272086143493652, 3.1254358291625977, 3.2428441047668457, 3.2630624771118164, 3.2592084407806396, 3.255235433578491, 3.2090084552764893, 3.264204502105713, 3.2671396732330322, 3.2347962856292725, 3.3195040225982666, 3.30202317237854, 3.3135199546813965, 3.297680139541626, 3.3291213512420654, 3.3242883682250977, 3.360891103744507, 3.4075045585632324, 3.316319704055786, 3.448855400085449, 3.3088295459747314, 3.5088143348693848, 3.377211332321167, 3.5215349197387695, 3.4458210468292236, 3.3725316524505615, 3.456930637359619, 3.452221155166626, 3.4281058311462402, 3.4168219566345215, 3.461782932281494, 3.489077091217041, 3.3884811401367188, 3.1276445388793945, 3.2956702709198, 3.229921340942383, 3.2848448753356934, 3.243237257003784, 3.30247163772583, 3.2347962856292725, 3.2987282276153564, 3.160318613052368, 3.2224130630493164, 3.365117073059082, 3.2857439517974854, 3.252777338027954, 3.370332956314087, 3.2289845943450928, 3.287200689315796, 3.3999407291412354, 3.338235378265381, 3.20150089263916, 3.2497873306274414, 3.202467918395996, 3.2824459075927734, 3.2213940620422363, 3.2892563343048096, 3.2066383361816406, 3.303354024887085, 3.3725316524505615, 3.2921807765960693, 3.3929216861724854, 3.4458210468292236, 3.325751781463623, 3.4075045585632324, 3.3516106605529785, 3.4481263160705566, 3.489077091217041, 3.3484909534454346, 3.337759256362915, 3.4057228565216064, 3.436028003692627, 3.3355064392089844, 3.4692070484161377, 3.3647537231445312, 3.5088143348693848, 3.435950756072998, 3.3976480960845947, 3.5215349197387695, 3.3718490600585938, 3.3956379890441895, 3.2013132572174072, 3.0700278282165527, 3.2667226791381836, 3.099111795425415, 3.0792393684387207, 3.2188339233398438, 3.074425458908081, 3.1521008014678955, 3.2272024154663086, 3.216857433319092, 3.117220640182495, 3.1768250465393066, 3.2367823123931885, 3.2662649154663086, 3.0859475135803223, 3.265204668045044, 3.252777338027954, 3.3086836338043213, 3.2472898960113525, 3.1985747814178467, 3.223259210586548, 3.2252955436706543, 3.181424140930176, 3.2088847160339355, 3.2481839656829834, 3.1379077434539795, 3.29801344871521, 3.3016316890716553, 3.291908025741577, 3.2090940475463867, 3.3038463592529297, 3.349013566970825, 3.337759256362915, 3.288841724395752, 3.294588088989258, 3.3282577991485596, 3.3195040225982666, 3.258953094482422, 3.358421802520752, 3.4489128589630127, 3.361154556274414, 3.341641426086426, 3.3945374488830566, 3.430643320083618, 3.210062026977539, 3.1474008560180664, 3.2806265354156494, 3.188227891921997, 3.2409842014312744, 3.20672345161438, 3.280478000640869, 3.2449631690979004, 3.2836194038391113, 3.1655654907226562, 3.3024139404296875, 3.196094036102295, 3.203383207321167, 3.2212839126586914, 3.2259275913238525, 3.250420570373535, 3.2824459075927734, 3.3023853302001953, 3.217714309692383, 3.189256191253662, 3.3286712169647217, 3.162613868713379, 3.2410097122192383, 3.3311378955841064, 3.2428042888641357, 3.287750720977783, 3.3062708377838135, 3.133347511291504, 3.2351677417755127, 3.2680881023406982, 3.2895758152008057, 3.3718490600585938, 3.3941633701324463, 3.385540246963501, 3.3252546787261963, 3.3725316524505615, 3.3613085746765137, 3.343073844909668, 3.3544254302978516, 3.4055209159851074, 3.3684749603271484, 3.341287136077881, 3.3767647743225098, 3.417299747467041, 3.38667631149292, 3.3387880325317383, 3.43245792388916, 3.372685194015503, 3.3538320064544678, 3.4281058311462402, 3.4436166286468506, 3.461782932281494, 3.3654510974884033, 3.4489128589630127, 3.430643320083618, 3.377211332321167, 3.4005990028381348, 3.3504421710968018, 3.3664793968200684, 3.3237907886505127, 3.3026225566864014, 3.3271095752716064, 3.2798779010772705, 3.3818817138671875, 3.386089563369751, 3.3410277366638184, 3.2677102088928223, 3.3632073402404785, 3.341470241546631, 3.2824044227600098, 3.5215349197387695, 3.3537063598632812, 3.4458210468292236, 3.3138649463653564, 3.303842544555664, 3.289829969406128, 3.3475217819213867, 3.371066093444824, 3.4553682804107666, 3.4117379188537598, 3.3232827186584473, 3.3658409118652344, 3.4168219566345215, 3.4106805324554443, 3.4075045585632324, 3.351895332336426, 3.5088143348693848, 3.489077091217041, 3.413961887359619, 3.432797431945801, 3.4633429050445557, 3.436028003692627, 3.448855400085449, 3.452221155166626, 3.2562880516052246, 3.3631746768951416, 3.372581958770752, 3.312737464904785, 3.3116798400878906, 3.2680881023406982, 3.3558878898620605, 3.351597785949707, 3.3756332397460938, 3.3088953495025635, 3.3379058837890625, 3.2428042888641357, 3.4357054233551025, 3.3632073402404785, 3.3260509967803955, 3.386089563369751, 3.4633429050445557, 3.472402811050415, 3.319085121154785, 3.4318954944610596, 3.3060483932495117, 3.292809009552002, 3.3750016689300537, 3.3265459537506104, 3.21181321144104, 3.4005990028381348, 3.316803216934204, 3.3252546787261963, 3.3786001205444336, 3.204206943511963, 3.359760046005249, 3.4479217529296875, 3.38667631149292, 3.4287383556365967, 3.3929216861724854, 3.5215349197387695, 3.4692070484161377, 3.452221155166626, 3.5088143348693848, 3.403538465499878], "loglift": [30.0, 29.0, 28.0, 27.0, 26.0, 25.0, 24.0, 23.0, 22.0, 21.0, 20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.08860000222921371, 0.08510000258684158, 0.08250000327825546, 0.08169999718666077, 0.07440000027418137, 0.07209999859333038, 0.07100000232458115, 0.07090000063180923, 0.07039999961853027, 0.07000000029802322, 0.0697999969124794, 0.06750000268220901, 0.0674000009894371, 0.0674000009894371, 0.06679999828338623, 0.06610000133514404, 0.06469999998807907, 0.06440000236034393, 0.06390000134706497, 0.06319999694824219, 0.06300000101327896, 0.06279999762773514, 0.06159999966621399, 0.06109999865293503, 0.0608999989926815, 0.05829999968409538, 0.05770000070333481, 0.05660000070929527, 0.05649999901652336, 0.056299999356269836, 0.056299999356269836, 0.05550000071525574, 0.05260000005364418, 0.05530000105500221, 0.04989999905228615, 0.053199999034404755, 0.049400001764297485, 0.040699999779462814, 0.04520000144839287, 0.026200000196695328, 0.0430000014603138, 0.040699999779462814, 0.03460000082850456, 0.04520000144839287, 0.02419999986886978, 0.026900000870227814, 0.024000000208616257, 0.017799999564886093, 0.000699999975040555, 0.026900000870227814, 0.10080000013113022, 0.09139999747276306, 0.08900000154972076, 0.08760000020265579, 0.08590000122785568, 0.08389999717473984, 0.08299999684095383, 0.0794999971985817, 0.0794999971985817, 0.07890000194311142, 0.07699999958276749, 0.07410000264644623, 0.07400000095367432, 0.07259999960660934, 0.0723000019788742, 0.07109999656677246, 0.07010000199079514, 0.06949999928474426, 0.06920000165700912, 0.06859999895095825, 0.06689999997615814, 0.06539999693632126, 0.06440000236034393, 0.0617000013589859, 0.06109999865293503, 0.06080000102519989, 0.06069999933242798, 0.060600001364946365, 0.06019999831914902, 0.05979999899864197, 0.05889999866485596, 0.05530000105500221, 0.05310000106692314, 0.05389999970793724, 0.0494999997317791, 0.051100000739097595, 0.04969999939203262, 0.03849999979138374, 0.0494999997317791, 0.041999999433755875, 0.04129999876022339, 0.027400000020861626, 0.07540000230073929, 0.07410000264644623, 0.06930000334978104, 0.06430000066757202, 0.0617000013589859, 0.061400000005960464, 0.06109999865293503, 0.06109999865293503, 0.05700000002980232, 0.05689999833703041, 0.05570000037550926, 0.05570000037550926, 0.053199999034404755, 0.052799999713897705, 0.05260000005364418, 0.05169999971985817, 0.05050000175833702, 0.0502999983727932, 0.05009999871253967, 0.05000000074505806, 0.049800001084804535, 0.04960000142455101, 0.0494999997317791, 0.0478999987244606, 0.04749999940395355, 0.04659999907016754, 0.04639999940991402, 0.046300001442432404, 0.045499999076128006, 0.04500000178813934, 0.04500000178813934, 0.04430000111460686, 0.04399999976158142, 0.043800000101327896, 0.04430000111460686, 0.043800000101327896, 0.033900000154972076, 0.028599999845027924, 0.03009999915957451, 0.039400000125169754, 0.02669999934732914, 0.03319999948143959, 0.0357000008225441, 0.02810000069439411, 0.032099999487400055, 0.027400000020861626, 0.03689999878406525, 0.02319999970495701, 0.02449999935925007, 0.030300000682473183, 0.00570000009611249, 0.0026000000070780516, 0.025800000876188278, 0.01510000042617321, 0.11349999904632568, 0.09910000115633011, 0.09809999912977219, 0.08309999853372574, 0.07810000330209732, 0.07699999958276749, 0.07590000331401825, 0.07240000367164612, 0.07150000333786011, 0.06939999759197235, 0.0689999982714653, 0.06840000301599503, 0.06539999693632126, 0.06080000102519989, 0.05979999899864197, 0.059700001031160355, 0.05959999933838844, 0.05950000137090683, 0.058800000697374344, 0.05860000103712082, 0.057999998331069946, 0.05779999867081642, 0.05700000002980232, 0.0568000003695488, 0.0544000007212162, 0.05389999970793724, 0.05310000106692314, 0.052799999713897705, 0.052299998700618744, 0.05220000073313713, 0.05009999871253967, 0.04910000041127205, 0.04809999838471413, 0.04690000042319298, 0.045499999076128006, 0.04619999974966049, 0.04360000044107437, 0.026900000870227814, 0.027699999511241913, 0.025100000202655792, 0.02800000086426735, 0.021199999377131462, 0.03420000150799751, 0.032099999487400055, 0.026799999177455902, 0.04129999876022339, 0.07859999686479568, 0.0746999979019165, 0.07069999724626541, 0.06800000369548798, 0.0632999986410141, 0.06210000067949295, 0.06109999865293503, 0.06019999831914902, 0.060100000351667404, 0.057500001043081284, 0.05739999935030937, 0.05730000138282776, 0.0568000003695488, 0.05400000140070915, 0.05310000106692314, 0.05209999904036522, 0.051899999380111694, 0.05090000107884407, 0.05050000175833702, 0.04989999905228615, 0.049800001084804535, 0.048500001430511475, 0.048500001430511475, 0.04839999973773956, 0.04820000007748604, 0.04800000041723251, 0.04780000075697899, 0.04749999940395355, 0.04749999940395355, 0.04699999839067459, 0.04600000008940697, 0.04600000008940697, 0.043800000101327896, 0.043699998408555984, 0.04129999876022339, 0.0414000004529953, 0.03370000049471855, 0.026599999517202377, 0.037700001150369644, 0.019500000402331352, 0.037700001150369644, 0.0017000000225380063, 0.02459999918937683, -0.00279999990016222, 0.009800000116229057, 0.02370000071823597, 0.004100000020116568, 0.002400000113993883, 0.007300000172108412, 0.009999999776482582, -0.0020000000949949026, -0.009700000286102295, 0.09269999712705612, 0.08910000324249268, 0.07989999651908875, 0.07440000027418137, 0.0714000016450882, 0.07079999893903732, 0.07050000131130219, 0.06769999861717224, 0.06549999862909317, 0.0649000033736229, 0.06469999998807907, 0.0608999989926815, 0.0608999989926815, 0.06040000170469284, 0.06030000001192093, 0.0575999990105629, 0.057500001043081284, 0.0568000003695488, 0.05530000105500221, 0.05510000139474869, 0.05490000173449516, 0.0544000007212162, 0.05389999970793724, 0.053700000047683716, 0.05249999836087227, 0.052000001072883606, 0.051899999380111694, 0.05169999971985817, 0.05090000107884407, 0.05090000107884407, 0.05040000006556511, 0.050700001418590546, 0.04830000177025795, 0.04919999837875366, 0.04439999908208847, 0.04129999876022339, 0.0471000000834465, 0.04800000041723251, 0.03959999978542328, 0.030899999663233757, 0.04479999840259552, 0.0203000009059906, 0.03880000114440918, 0.009499999694526196, 0.020400000736117363, 0.028699999675154686, -0.0066999997943639755, 0.03420000150799751, 0.027400000020861626, 0.14470000565052032, 0.13169999420642853, 0.1242000013589859, 0.11949999630451202, 0.11490000039339066, 0.11479999870061874, 0.1071000024676323, 0.10530000180006027, 0.10339999943971634, 0.10289999842643738, 0.09960000216960907, 0.09520000219345093, 0.09520000219345093, 0.09260000288486481, 0.09200000017881393, 0.08950000256299973, 0.08630000054836273, 0.08150000125169754, 0.08089999854564667, 0.08030000329017639, 0.08009999990463257, 0.07930000126361847, 0.07810000330209732, 0.07490000128746033, 0.07320000231266022, 0.0714000016450882, 0.07079999893903732, 0.06970000267028809, 0.06960000097751617, 0.06920000165700912, 0.06840000301599503, 0.06620000302791595, 0.06419999897480011, 0.06560000032186508, 0.06499999761581421, 0.05950000137090683, 0.0560000017285347, 0.06729999929666519, 0.043299999088048935, 0.01979999989271164, 0.041200000792741776, 0.04540000110864639, 0.03020000085234642, 0.01860000006854534, 0.08209999650716782, 0.0763000026345253, 0.07429999858140945, 0.06970000267028809, 0.06769999861717224, 0.06710000336170197, 0.06499999761581421, 0.06400000303983688, 0.05939999967813492, 0.058400001376867294, 0.05820000171661377, 0.057500001043081284, 0.05739999935030937, 0.05719999969005585, 0.0568000003695488, 0.056699998676776886, 0.056299999356269836, 0.05530000105500221, 0.054499998688697815, 0.05429999902844429, 0.05249999836087227, 0.05169999971985817, 0.05139999836683273, 0.050999999046325684, 0.050599999725818634, 0.049400001764297485, 0.049400001764297485, 0.049300000071525574, 0.04910000041127205, 0.048900000751018524, 0.048700001090765, 0.04740000143647194, 0.04270000010728836, 0.04179999977350235, 0.04439999908208847, 0.039799999445676804, 0.039000000804662704, 0.0406000018119812, 0.03790000081062317, 0.030400000512599945, 0.03460000082850456, 0.03819999843835831, 0.032499998807907104, 0.024299999698996544, 0.028999999165534973, 0.03720000013709068, 0.016599999740719795, 0.029200000688433647, 0.03310000151395798, 0.012000000104308128, 0.007300000172108412, 0.1046999990940094, 0.09189999848604202, 0.08100000023841858, 0.07150000333786011, 0.06729999929666519, 0.06589999794960022, 0.06589999794960022, 0.0649000033736229, 0.0640999972820282, 0.06400000303983688, 0.06369999796152115, 0.06360000371932983, 0.06340000033378601, 0.06270000338554382, 0.061900001019239426, 0.061000000685453415, 0.059700001031160355, 0.05909999832510948, 0.05900000035762787, 0.05790000036358833, 0.05770000070333481, 0.05719999969005585, 0.0568000003695488, 0.055399999022483826, 0.05530000105500221, 0.0551999993622303, 0.054499998688697815, 0.0544000007212162, 0.05420000106096268, 0.05420000106096268, 0.054099999368190765, 0.05209999904036522, 0.05220000073313713, 0.0494999997317791, 0.05270000174641609, 0.03359999880194664, 0.03579999879002571, 0.042399998754262924, 0.037300001829862595, 0.02889999933540821, 0.033399999141693115, 0.02979999966919422, 0.0284000001847744, 0.11840000003576279, 0.1136000007390976, 0.10159999877214432, 0.10080000013113022, 0.09690000116825104, 0.09640000015497208, 0.09459999948740005, 0.09459999948740005, 0.0940999984741211, 0.093299999833107, 0.0925000011920929, 0.08810000121593475, 0.08749999850988388, 0.08560000360012054, 0.08399999886751175, 0.08389999717473984, 0.08370000123977661, 0.08290000259876251, 0.0828000009059906, 0.08209999650716782, 0.07819999754428864, 0.07620000094175339, 0.07500000298023224, 0.07440000027418137, 0.07159999758005142, 0.07090000063180923, 0.0706000030040741, 0.07050000131130219, 0.06989999860525131, 0.06830000132322311, 0.06780000030994415, 0.06599999964237213, 0.06710000336170197, 0.06499999761581421, 0.066600002348423, 0.05420000106096268, 0.05700000002980232, 0.05689999833703041, 0.046300001442432404, 0.06040000170469284], "logprob": [30.0, 29.0, 28.0, 27.0, 26.0, 25.0, 24.0, 23.0, 22.0, 21.0, 20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, -6.639200210571289, -6.633500099182129, -6.646699905395508, -6.69290018081665, -6.654099941253662, -6.683499813079834, -6.6666998863220215, -6.696899890899658, -6.642499923706055, -6.62470006942749, -6.6381001472473145, -6.658999919891357, -6.678599834442139, -6.663599967956543, -6.666299819946289, -6.695300102233887, -6.664000034332275, -6.664100170135498, -6.653299808502197, -6.686600208282471, -6.661300182342529, -6.66349983215332, -6.655300140380859, -6.69980001449585, -6.648499965667725, -6.672100067138672, -6.651599884033203, -6.672599792480469, -6.7027997970581055, -6.702899932861328, -6.64139986038208, -6.653299808502197, -6.634799957275391, -6.6605000495910645, -6.647299766540527, -6.660099983215332, -6.652699947357178, -6.637400150299072, -6.649600028991699, -6.633500099182129, -6.652100086212158, -6.651800155639648, -6.6479997634887695, -6.654900074005127, -6.6508002281188965, -6.654799938201904, -6.654399871826172, -6.656899929046631, -6.655399799346924, -6.659299850463867, -6.570199966430664, -6.640600204467773, -6.648600101470947, -6.625199794769287, -6.616700172424316, -6.572199821472168, -6.625699996948242, -6.631100177764893, -6.6097002029418945, -6.6092000007629395, -6.599899768829346, -6.651700019836426, -6.607699871063232, -6.649199962615967, -6.60230016708374, -6.607399940490723, -6.617700099945068, -6.637899875640869, -6.650000095367432, -6.639599800109863, -6.651899814605713, -6.634200096130371, -6.617499828338623, -6.650400161743164, -6.65749979019165, -6.671800136566162, -6.6269001960754395, -6.649400234222412, -6.650199890136719, -6.639200210571289, -6.656199932098389, -6.632699966430664, -6.621600151062012, -6.627699851989746, -6.623300075531006, -6.631199836730957, -6.63100004196167, -6.621200084686279, -6.637700080871582, -6.635200023651123, -6.635900020599365, -6.637899875640869, -6.661600112915039, -6.633600234985352, -6.68120002746582, -6.644999980926514, -6.684199810028076, -6.640699863433838, -6.6768999099731445, -6.656400203704834, -6.688300132751465, -6.665500164031982, -6.692500114440918, -6.6743998527526855, -6.666100025177002, -6.68120002746582, -6.667799949645996, -6.625400066375732, -6.676499843597412, -6.64900016784668, -6.6596999168396, -6.656499862670898, -6.6956000328063965, -6.62060022354126, -6.670199871063232, -6.680099964141846, -6.678999900817871, -6.68779993057251, -6.644700050354004, -6.686800003051758, -6.631800174713135, -6.6971001625061035, -6.642099857330322, -6.642399787902832, -6.660299777984619, -6.663099765777588, -6.666399955749512, -6.668700218200684, -6.6468000411987305, -6.642499923706055, -6.6468000411987305, -6.662600040435791, -6.646100044250488, -6.654600143432617, -6.65880012512207, -6.652599811553955, -6.6585001945495605, -6.655600070953369, -6.6616997718811035, -6.655300140380859, -6.656199932098389, -6.659200191497803, -6.6539998054504395, -6.65339994430542, -6.660299777984619, -6.660900115966797, -6.622000217437744, -6.627999782562256, -6.651599884033203, -6.677499771118164, -6.633200168609619, -6.6433000564575195, -6.657599925994873, -6.636099815368652, -6.6768999099731445, -6.71120023727417, -6.662199974060059, -6.638199806213379, -6.650599956512451, -6.669099807739258, -6.641600131988525, -6.676499843597412, -6.680799961090088, -6.662099838256836, -6.645400047302246, -6.686699867248535, -6.665599822998047, -6.664299964904785, -6.661600112915039, -6.638500213623047, -6.690800189971924, -6.642000198364258, -6.644999980926514, -6.715000152587891, -6.68149995803833, -6.676499843597412, -6.6585001945495605, -6.643400192260742, -6.660600185394287, -6.658599853515625, -6.666200160980225, -6.667799949645996, -6.664400100708008, -6.646299839019775, -6.6493000984191895, -6.649899959564209, -6.653900146484375, -6.651500225067139, -6.658599853515625, -6.660299777984619, -6.660900115966797, -6.663899898529053, -6.644999980926514, -6.673299789428711, -6.666999816894531, -6.694699764251709, -6.658199787139893, -6.683300018310547, -6.670499801635742, -6.706600189208984, -6.706099987030029, -6.679699897766113, -6.662700176239014, -6.6828999519348145, -6.6793999671936035, -6.713600158691406, -6.674600124359131, -6.711900234222412, -6.673799991607666, -6.69290018081665, -6.701200008392334, -6.6722002029418945, -6.693600177764893, -6.726900100708008, -6.690100193023682, -6.683899879455566, -6.685299873352051, -6.686699867248535, -6.701200008392334, -6.684500217437744, -6.683599948883057, -6.693999767303467, -6.669099807739258, -6.674499988555908, -6.673099994659424, -6.678100109100342, -6.671000003814697, -6.672399997711182, -6.669099807739258, -6.662399768829346, -6.678400039672852, -6.65749979019165, -6.680699825286865, -6.6579999923706055, -6.673399925231934, -6.65880012512207, -6.668000221252441, -6.6757001876831055, -6.670499801635742, -6.673600196838379, -6.6757001876831055, -6.676300048828125, -6.67519998550415, -6.675099849700928, -6.601900100708008, -6.6855998039245605, -6.642499923706055, -6.668099880218506, -6.654200077056885, -6.667600154876709, -6.649799823760986, -6.673299789428711, -6.655900001525879, -6.699399948120117, -6.680200099945068, -6.640600204467773, -6.6645002365112305, -6.675099849700928, -6.639699935913086, -6.685200214385986, -6.667399883270264, -6.634399890899658, -6.654200077056885, -6.696300029754639, -6.68149995803833, -6.696700096130371, -6.672500133514404, -6.691500186920166, -6.671800136566162, -6.697700023651123, -6.668099880218506, -6.647600173950195, -6.672500133514404, -6.642399787902832, -6.627399921417236, -6.662600040435791, -6.640699863433838, -6.656400203704834, -6.632800102233887, -6.624100208282471, -6.65939998626709, -6.6616997718811035, -6.649899959564209, -6.649799823760986, -6.665599822998047, -6.6508002281188965, -6.662799835205078, -6.650199890136719, -6.660299777984619, -6.6631999015808105, -6.662700176239014, -6.66540002822876, -6.66510009765625, -6.6066999435424805, -6.661600112915039, -6.60699987411499, -6.664400100708008, -6.6753997802734375, -6.631199836730957, -6.684800148010254, -6.661600112915039, -6.639900207519531, -6.643700122833252, -6.678400039672852, -6.663899898529053, -6.645199775695801, -6.638700008392334, -6.696199893951416, -6.642099857330322, -6.649199962615967, -6.636899948120117, -6.656199932098389, -6.671999931335449, -6.6645002365112305, -6.664599895477295, -6.679599761962891, -6.674099922180176, -6.663700103759766, -6.699999809265137, -6.6508002281188965, -6.6508002281188965, -6.6539998054504395, -6.679699897766113, -6.651500225067139, -6.640100002288818, -6.645500183105469, -6.65880012512207, -6.657700061798096, -6.6529998779296875, -6.65910005569458, -6.666299819946289, -6.660200119018555, -6.657100200653076, -6.661499977111816, -6.663099765777588, -6.662600040435791, -6.663599967956543, -6.666500091552734, -6.692200183868408, -6.652599811553955, -6.685800075531006, -6.67140007019043, -6.682600021362305, -6.6620001792907715, -6.673900127410889, -6.6666998863220215, -6.7042999267578125, -6.662099838256836, -6.6956000328063965, -6.693399906158447, -6.688000202178955, -6.686999797821045, -6.679500102996826, -6.670100212097168, -6.66510009765625, -6.691800117492676, -6.700900077819824, -6.659900188446045, -6.711900234222412, -6.687699794769287, -6.660699844360352, -6.688000202178955, -6.6753997802734375, -6.6697998046875, -6.723599910736084, -6.691800117492676, -6.68179988861084, -6.67549991607666, -6.652100086212158, -6.650199890136719, -6.65369987487793, -6.669000148773193, -6.659599781036377, -6.663599967956543, -6.667500019073486, -6.666800022125244, -6.659200191497803, -6.665900230407715, -6.670400142669678, -6.665599822998047, -6.661900043487549, -6.666100025177002, -6.6722002029418945, -6.66510009765625, -6.670100212097168, -6.671800136566162, -6.670899868011475, -6.671199798583984, -6.56850004196167, -6.609499931335449, -6.595900058746338, -6.6107001304626465, -6.6305999755859375, -6.625100135803223, -6.639999866485596, -6.636199951171875, -6.649799823760986, -6.656300067901611, -6.649199962615967, -6.663599967956543, -6.633200168609619, -6.632699966430664, -6.6468000411987305, -6.6697998046875, -6.642399787902832, -6.649400234222412, -6.667399883270264, -6.598199844360352, -6.647200107574463, -6.62060022354126, -6.660099983215332, -6.6645002365112305, -6.668900012969971, -6.651599884033203, -6.645299911499023, -6.620699882507324, -6.633500099182129, -6.659800052642822, -6.647200107574463, -6.634200096130371, -6.635799884796143, -6.639500141143799, -6.6528000831604, -6.626100063323975, -6.629499912261963, -6.644700050354004, -6.6442999839782715, -6.643899917602539, -6.647299766540527, -6.64709997177124, -6.647500038146973, -6.616000175476074, -6.588500022888184, -6.597700119018555, -6.616399765014648, -6.62060022354126, -6.634399890899658, -6.6097002029418945, -6.611000061035156, -6.604300022125244, -6.625100135803223, -6.617099761962891, -6.650400161743164, -6.593299865722656, -6.616499900817871, -6.629199981689453, -6.611499786376953, -6.589000225067139, -6.587299823760986, -6.632500171661377, -6.599699974060059, -6.640999794006348, -6.64709997177124, -6.623600006103516, -6.638700008392334, -6.676499843597412, -6.620200157165527, -6.645299911499023, -6.64300012588501, -6.627600193023682, -6.682199954986572, -6.635300159454346, -6.611199855804443, -6.627999782562256, -6.617800235748291, -6.626699924468994, -6.601900100708008, -6.613999843597412, -6.619100093841553, -6.613399982452393, -6.629799842834473]}, "token.table": {"Topic": [], "Freq": [], "Term": []}, "R": 30, "lambda.step": 0.01, "plot.opts": {"xlab": "PC1", "ylab": "PC2"}, "topic.order": [3, 7, 10, 9, 4, 2, 1, 6, 5, 8]};
    
    function LDAvis_load_lib(url, callback){
      var s = document.createElement('script');
      s.src = url;
      s.async = true;
      s.onreadystatechange = s.onload = callback;
      s.onerror = function(){console.warn("failed to load library " + url);};
      document.getElementsByTagName("head")[0].appendChild(s);
    }
    
    if(typeof(LDAvis) !== "undefined"){
       // already loaded: just create the visualization
       !function(LDAvis){
           new LDAvis("#" + "ldavis_el8715855864430882865459121", ldavis_el8715855864430882865459121_data);
       }(LDAvis);
    }else if(typeof define === "function" && define.amd){
       // require.js is available: use it to load d3/LDAvis
       require.config({paths: {d3: "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min"}});
       require(["d3"], function(d3){
          window.d3 = d3;
          LDAvis_load_lib("https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.js", function(){
            new LDAvis("#" + "ldavis_el8715855864430882865459121", ldavis_el8715855864430882865459121_data);
          });
        });
    }else{
        // require.js not available: dynamically load d3 & LDAvis
        LDAvis_load_lib("https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js", function(){
             LDAvis_load_lib("https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.js", function(){
                     new LDAvis("#" + "ldavis_el8715855864430882865459121", ldavis_el8715855864430882865459121_data);
                })
             });
    }
    </script>



Train LDA model
---------------

.. code:: ipython3

    lda = malaya.topic_model.lda(corpus,10,stemming=None,vectorizer='skip-gram',ngram=(1,4),skip=3)

Print topics
^^^^^^^^^^^^

.. code:: ipython3

    lda.top_topics(5, top_n = 10, return_df = True)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>topic 0</th>
          <th>topic 1</th>
          <th>topic 2</th>
          <th>topic 3</th>
          <th>topic 4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>menteri</td>
          <td>kerajaan</td>
          <td>pilihan raya</td>
          <td>jho</td>
          <td>malaysia</td>
        </tr>
        <tr>
          <th>1</th>
          <td>parti</td>
          <td>awam</td>
          <td>raya</td>
          <td>low</td>
          <td>rakyat</td>
        </tr>
        <tr>
          <th>2</th>
          <td>seri</td>
          <td>terima</td>
          <td>pilihan</td>
          <td>jho low</td>
          <td>negara</td>
        </tr>
        <tr>
          <th>3</th>
          <td>menteri seri</td>
          <td>pendidikan</td>
          <td>ph</td>
          <td>tuntutan sivil doj</td>
          <td>kerajaan</td>
        </tr>
        <tr>
          <th>4</th>
          <td>kebenaran</td>
          <td>mencapai</td>
          <td>parti</td>
          <td>sivil doj</td>
          <td>rakyat malaysia</td>
        </tr>
        <tr>
          <th>5</th>
          <td>negara</td>
          <td>kemajuan</td>
          <td>rakyat</td>
          <td>berjalan</td>
          <td>menteri</td>
        </tr>
        <tr>
          <th>6</th>
          <td>kawasan</td>
          <td>pelbagai</td>
          <td>jppm</td>
          <td>doj</td>
          <td>projek</td>
        </tr>
        <tr>
          <th>7</th>
          <td>perdana menteri</td>
          <td>laporan</td>
          <td>air</td>
          <td>perniagaan</td>
          <td>perdana</td>
        </tr>
        <tr>
          <th>8</th>
          <td>perdana seri</td>
          <td>terima kasih</td>
          <td>kerja</td>
          <td>tuntutan</td>
          <td>isu</td>
        </tr>
        <tr>
          <th>9</th>
          <td>seri razak</td>
          <td>kasih</td>
          <td>bertanding</td>
          <td>sivil</td>
          <td>tindakan</td>
        </tr>
      </tbody>
    </table>
    </div>



Important sentences based on topics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: ipython3

    lda.get_sentences(5)




.. parsed-literal::

    ['negara membangun malaysia memainkan peranan berkongsi pengalaman kemahirannya membangunkan kawasan bandar',
     'negara membangun malaysia memainkan peranan berkongsi pengalaman kemahirannya membangunkan kawasan bandar',
     'diselesaikan perdana menteri seri najib razak memberitahu rakan parti komponen jemaah menteri diperjelaskan robert kuok diterima',
     'perdana menteri seri najib razak keputusan umno mesyuarat umno bahagian cawangan selesai april',
     'perdana menteri seri najib razak mempertikaikan sumbangan robert kuok ekonomi negara']



Get topics
^^^^^^^^^^

.. code:: ipython3

    lda.get_topics(10)




.. parsed-literal::

    [(0,
      'menteri parti seri menteri seri kebenaran negara kawasan perdana menteri perdana seri seri razak'),
     (1,
      'kerajaan awam terima pendidikan mencapai kemajuan pelbagai laporan terima kasih kasih'),
     (2, 'pilihan raya raya pilihan ph parti rakyat jppm air kerja bertanding'),
     (3,
      'jho low jho low tuntutan sivil doj sivil doj berjalan doj perniagaan tuntutan sivil'),
     (4,
      'malaysia rakyat negara kerajaan rakyat malaysia menteri projek perdana isu tindakan'),
     (5,
      'hutang mdb parti malaysia diselesaikan kelulusan kewangan harapan islam pas'),
     (6,
      'bahasa masyarakat syarikat ahli ilmu status wang negara sokongan keluarga'),
     (7,
      'berkongsi pengalaman negara selatan pengalaman pembangunannya negara selatan negara selatan pengalaman negara selatan berkongsi pembangunannya negara selatan pembangunannya negara selatan negara malaysia pengalaman berkongsi'),
     (8,
      'ros umno parti asli bersatu pelbagai pemilihan pertumbuhan perlembagaan keputusan'),
     (9,
      'negara negara bidang harga membantu negara perancangan ekonomi negara maju perancangan negara maju ekonomi kewangan membantu negara bidang membantu negara bidang ekonomi membantu negara bidang perancangan membantu negara maju')]



Visualize topics
^^^^^^^^^^^^^^^^

.. code:: ipython3

    lda.visualize_topics(notebook_mode = True)


.. parsed-literal::

    /usr/local/lib/python3.7/site-packages/past/types/oldstr.py:5: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working
      from collections import Iterable




.. raw:: html

    
    <link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.css">
    
    
    <div id="ldavis_el8739156648247841161749766"></div>
    <script type="text/javascript">
    
    var ldavis_el8739156648247841161749766_data = {"mdsDat": {"x": [0.24257568821742445, -0.22225656879202058, 0.023605323616853226, -0.010286592277672613, -0.024543331444407113, -0.019219819589648947, -0.005212228140149834, 0.0025040550404343146, 0.006715038224336561, 0.006118435144850352], "y": [-0.15304428580264032, -0.14690305026361963, 0.20878423685696215, 0.05892234905103484, -0.006782163625745933, -0.00298608875739497, 0.024233530249201243, 0.013560230407235741, -0.008278155051376957, 0.012493396936344651], "topics": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "cluster": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "Freq": [28.04266656112074, 17.69702228531917, 12.707611022132493, 8.522162157981844, 7.837962755223457, 5.829371991812138, 5.809778713552299, 5.125959202606012, 4.419136136310243, 4.008329173941587]}, "tinfo": {"Category": ["Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic4", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic5", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic6", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic7", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic8", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic9", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10", "Topic10"], "Freq": [14.0, 25.0, 15.0, 10.0, 7.0, 15.0, 27.0, 7.0, 5.0, 11.0, 7.0, 4.0, 9.0, 7.0, 5.0, 4.0, 3.0, 6.0, 6.0, 3.0, 3.0, 3.0, 6.0, 6.0, 7.0, 4.0, 4.0, 5.0, 7.0, 3.0, 7.183500699483656, 7.183500699483656, 7.183500699483656, 7.183500699483656, 7.183500699483656, 7.183500699483656, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 3.636092946634714, 4.52294324058784, 7.183498938708765, 3.636092946634714, 3.636092946634714, 3.636092946634714, 4.522950425276794, 4.522956877982932, 5.409759444314292, 3.6360930760057193, 3.6360930760057193, 3.636092946634714, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.3754152309147507, 3.375392046082799, 3.375302604838069, 4.929862327029026, 3.375432339653266, 3.375419867042518, 3.1900826755638954, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.41203712313563, 2.4120328181655455, 2.4120178297310493, 2.4120200268484533, 2.411994116933861, 2.4119904079183123, 1.6339608572452746, 1.6339608572452746, 3.190118631874372, 3.1901241301606404, 3.9456240468236574, 3.4580750994051725, 2.412062468305017, 2.412044984796134, 2.4120440607386273, 2.4120419221072313, 2.714178758194763, 2.052186034731225, 2.0521860346516627, 2.0521860343870895, 2.052186034332125, 2.0521860343100395, 2.0521860343100395, 2.0521860336826507, 2.052185064085642, 2.052185064085642, 2.052185064085642, 2.052185064085642, 2.052184586038526, 2.052183040413113, 2.052182188795349, 2.0521739024145598, 2.0521720893544106, 2.0521701182962855, 2.0521616308580657, 4.700179705568401, 2.7141853139490855, 1.390190539530137, 1.390190539530137, 1.390190539530137, 1.390190539530137, 1.3901905393362388, 1.3901905393362388, 1.3901905393362388, 1.3901905393362388, 1.3901905393362388, 9.996163192793162, 1.3901905393362388, 2.714192473283454, 3.278965338798396, 2.7141942705977047, 2.0521329012702445, 2.714201219540514, 2.052182973361785, 2.052192309337674, 2.052188252070557, 10.405495951831002, 2.714207699527079, 6.569764128400889, 7.766821635248961, 3.0342655905954268, 4.038170729578491, 3.333096953038601, 2.7141911590250807, 3.5385023764208707, 3.3761733460502366, 2.7141742701056306, 2.7141468517178673, 2.505262908432179, 2.052227145698799, 2.7453637465670284, 2.0757655821930756, 2.0757605620728867, 2.0757605620728867, 2.075761438902428, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 2.7453778278779355, 2.0757674606178393, 2.7453045283481856, 4.084664560161407, 1.40616378170394, 2.075761749626497, 2.0757372442836597, 2.075738105050733, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.40616378170394, 1.4061888965753793, 1.4061816400607394, 1.4061798175412403, 1.4061664893165833, 1.40616378170394, 4.184388957029959, 2.416337284932036, 2.416337284461446, 2.416303218474641, 1.8269867275667278, 1.8269867275638632, 1.8269867275638632, 1.826986727526456, 1.8269867275226743, 1.8269867275216227, 1.8269867275216227, 1.8269867274775695, 1.8269867274090572, 1.8269867269621263, 1.8269867257522103, 1.8269867252443488, 1.8269824795665666, 1.8269495912387435, 1.826934905820948, 1.8269177871503723, 1.237636170157779, 1.237636170157779, 1.237636170157779, 1.237636170157779, 1.237636170157779, 1.237636170157779, 1.237636170157779, 1.237636170157779, 1.237636170157779, 1.2376361701448182, 3.5950639215320535, 1.826981867652521, 1.8270109268009886, 2.41633050922785, 2.968535891397833, 3.0057505510123192, 1.746233366468359, 1.8269867366852355, 1.8269503229538464, 1.82698133411009, 2.4163210252595246, 1.827004448901147, 1.8269593920942744, 6.468547495541211, 2.3892843504703585, 2.389284350460351, 2.3892843503611365, 2.389280048853407, 1.8065320698145468, 1.8065320697497587, 1.806532069566006, 1.806530172418955, 1.8065271875586633, 1.8065174864629245, 1.8065172285217093, 1.8065155720183843, 1.8065155720183843, 2.9720395865215403, 2.972034067635925, 2.38927688546992, 2.972040871837561, 1.223779789144566, 1.2237797890835793, 1.2237797890402615, 1.2237797890402615, 1.2237797890402615, 1.2237797890402615, 1.2237797890060136, 1.2237797890060136, 1.223779788909457, 1.223779788909457, 1.2237797887988449, 1.2237797886014885, 5.78982179105825, 2.9581101459771846, 2.9720360343436396, 1.8065435174965914, 1.80653125637923, 1.8065357972723284, 1.8065452690357466, 1.8065357878160093, 5.303067906288623, 2.389301826045521, 2.389333082829479, 1.7814981610269323, 3.538761107546207, 1.8065475285405947, 1.8065288393034133, 4.009278679135473, 1.750512736291436, 1.750512736291436, 1.7505127361353015, 1.7505097861073888, 1.750509058299234, 1.7505090582618816, 1.7505090582618819, 1.7503253071913, 2.8798890633558747, 2.3152140433900708, 1.1858331719584239, 1.1858331719584239, 1.185833171956407, 1.185833171956407, 1.185833171956407, 1.185833171956407, 1.185833171956407, 1.185833171956407, 1.1858331717206234, 1.1858331713212134, 1.1858331713212134, 1.1858331712522991, 1.185833169567288, 1.1858318248558164, 1.1858318248557982, 1.1858318248557982, 1.1858318248557982, 1.185828371701794, 1.1858285038875562, 2.782196909764212, 3.878139158678512, 1.7505171629968144, 3.4446078470989243, 2.8590277307968766, 2.3152293195614573, 3.5576397854884547, 2.2665670844026566, 1.9287381875955765, 1.750536125248161, 1.7505136271927675, 1.1989980936206743, 1.1990258904336497, 1.1858629684055138, 1.1858537716897604, 1.1858512898042934, 1.1858468238531343, 1.1858411031413698, 1.1858408557988527, 3.8758364176448845, 3.304761717123677, 2.790718227500511, 2.790718214826174, 2.243486800580735, 2.243486744535193, 3.872013190450658, 1.6963245499533453, 1.6963245499533453, 1.6963237318828572, 1.6963182685192517, 1.6963182685192522, 2.790716601163983, 1.1491230821418976, 1.1491230821418976, 1.1491230821418976, 1.1491230821418976, 1.1491230821418976, 1.1491230821418976, 1.1491230821418976, 1.1491230821418976, 1.1491230821418976, 1.1491217649271728, 1.1491217649271728, 1.1491217649271728, 1.1491217649271728, 1.1491217649271728, 1.1491217649271728, 1.1491217649271728, 1.1491217649271728, 2.2434931247211356, 1.1491217649271728, 2.243495843455943, 2.594703160558531, 1.6963250602510633, 1.6963250602510633, 1.696333401569478, 2.243545912159571, 1.6156578183939478, 2.234976794564289, 1.8226064122089354, 1.1491289926219213, 1.149126305225943, 3.0649178662752874, 3.0649178662752874, 3.0649178662752874, 2.060030275515441, 2.0600276715382453, 2.0600273454745004, 1.557583425381817, 1.557583425381817, 1.5575832331253792, 1.5575831546591576, 1.5575737796632887, 1.055137819967042, 1.055137819907252, 1.0551378198386028, 1.0551378197388661, 1.0551378197388661, 1.0551378196767012, 1.0551378190954381, 1.0551378190359226, 1.0551378173347248, 1.0551362490365546, 1.0551362490365546, 1.0551362490365546, 1.0551362490365546, 1.0551359393932047, 1.0551359393932047, 1.0551358147821916, 1.055135341006413, 1.055135340259913, 1.0551193473996037, 2.5624936366713773, 2.060030605169206, 1.557588228387241, 1.557586625104954, 2.017737739060904, 1.5575857197885359, 1.475497697629274, 2.2888688448396044, 2.060056723629828, 1.557585463928126, 1.2624588495933688, 1.5576265128044244, 1.557588526940739, 1.2992889583259828, 1.0551510670024282, 1.0551443886167877, 1.0551440723746996, 1.0551430490428357, 1.0551427090864436], "Term": ["rakyat", "malaysia", "parti", "mdb", "hutang", "kerajaan", "negara", "umno", "low", "menteri", "asli", "jho", "projek", "perniagaan", "ros", "bahasa", "jho low", "masyarakat", "pelbagai", "pilihan raya", "pilihan", "raya", "rakyat malaysia", "ahli", "keputusan", "ph", "doj", "kewangan", "syarikat", "berjalan", "pembangunannya negara selatan", "berkongsi pembangunannya negara selatan", "pengalaman negara selatan", "berkongsi pengalaman negara selatan", "pengalaman pembangunannya negara selatan", "negara selatan", "kesediaan malaysia pembangunannya negara", "berkongsi pembangunannya negara", "kesediaan malaysia pengalaman negara", "kesediaan pengalaman pembangunannya negara", "pembangunannya negara", "pengalaman pembangunannya negara", "malaysia berkongsi negara selatan", "pengalaman negara negara selatan", "malaysia berkongsi pembangunannya negara", "malaysia berkongsi pengalaman negara", "malaysia berkongsi pengalaman pembangunannya", "pengalaman negara", "malaysia berkongsi negara", "negara selatan selatan", "pembangunannya negara negara selatan", "pembangunannya negara selatan selatan", "teknikal malaysia berkongsi pengalaman", "teknikal malaysia berkongsi", "teknikal malaysia", "pembangunannya selatan", "berkongsi pengalaman negara", "program kerjasama teknikal malaysia", "berkongsi pengalaman pembangunannya negara", "berkongsi pengalaman pembangunannya selatan", "kesediaan malaysia berkongsi negara", "malaysia pembangunannya negara", "malaysia pembangunannya negara selatan", "malaysia pengalaman negara", "malaysia pengalaman negara selatan", "malaysia pengalaman pembangunannya negara", "berkongsi pengalaman", "negara", "selatan", "pengalaman pembangunannya selatan", "pengalaman negara selatan selatan", "berkongsi", "pengalaman", "malaysia", "malaysia berkongsi", "malaysia berkongsi pengalaman", "negara negara selatan", "negara maju ekonomi", "negara bidang perancangan", "negara maju perancangan", "negara maju ekonomi kewangan", "negara maju bidang perancangan", "negara maju bidang kewangan", "negara maju bidang ekonomi", "negara maju bidang", "negara maju", "negara perancangan", "negara perancangan ekonomi", "negara perancangan ekonomi kewangan", "negara bidang perancangan kewangan", "negara bidang perancangan ekonomi", "negara bidang ekonomi kewangan", "negara maju perancangan kewangan", "negara bidang ekonomi", "membantu negara perancangan ekonomi", "membantu negara perancangan", "membantu negara maju perancangan", "membantu negara maju ekonomi", "membantu negara maju bidang", "membantu negara maju", "membantu negara bidang perancangan", "membantu negara bidang ekonomi", "membantu negara bidang", "membantu negara", "negara maju perancangan ekonomi", "kwsp", "langkah", "negara", "negara bidang", "harga", "kebenaran", "perdana razak", "perdana menteri seri razak", "seri razak", "perdana seri najib razak", "perdana seri razak", "menteri najib razak", "seri najib", "menteri razak", "perdana seri najib", "najib razak", "menteri seri najib", "perdana najib", "menteri najib", "menteri seri najib razak", "seri najib razak", "perdana najib razak", "perdana menteri najib", "menteri seri razak", "perdana menteri najib razak", "perdana menteri razak", "perdana menteri seri najib", "razak", "perdana menteri seri", "kawasan bandar", "keputusan umno", "membangunkan", "menangguhkan", "pemilihan parti", "memainkan peranan pengalaman", "memainkan peranan membangunkan kawasan", "menteri seri", "seri", "menteri", "parti", "negara", "kawasan", "perdana menteri", "perdana seri", "serius", "kepimpinan negara", "rakyat kepimpinan", "pertimbangan", "tentera", "pesara tentera", "pesara", "anti", "kegiatan", "kegiatan kehidupan penduduk", "kegiatan penduduk", "kegiatan kehidupan", "memilih", "penduduk", "menjadikan", "membentuk", "melayu", "hak", "gaji", "rakyat malaysia", "kepimpinan", "rakyat malaysia kepimpinan negara", "rakyat malaysia kepimpinan", "malaysia kepimpinan", "malaysia kepimpinan negara", "pertimbangan sewajarnya menulis kenyataan", "pertimbangan sewajarnya", "pertimbangan kenyataan", "pertimbangan sewajarnya kenyataan", "pertimbangan sewajarnya menulis", "rakyat", "pertimbangan menulis kenyataan", "negeri", "tindakan", "rumah", "kemudahan", "cina", "membayar", "penjelasan", "nhrap", "malaysia", "kementerian", "kerajaan", "negara", "mengambil", "menteri", "isu", "undi", "projek", "perdana", "perdana menteri", "perniagaan", "pendapatan", "kenyataan", "terima", "kemajuan", "kasih", "terima kasih", "laporan", "meningkatkan bidang pembelajaran pengajaran", "pendidikan proses pembelajaran", "pendidikan proses pembelajaran pengajaran", "pendidikan proses pengajaran", "pengajaran", "kemajuan pendidikan pengajaran", "kemajuan pendidikan proses", "kerajaan pendidikan proses pembelajaran", "kemajuan pendidikan proses pembelajaran", "pendidikan pengajaran", "kerajaan pendidikan proses", "kerajaan pendidikan", "kerajaan meningkatkan proses pembelajaran", "bidang pengajaran", "bidang pendidikan proses pengajaran", "pendidikan proses", "pendidikan pembelajaran", "pendidikan pembelajaran pengajaran", "kemajuan proses pembelajaran", "kemajuan bidang pembelajaran", "kemajuan bidang pembelajaran pengajaran", "kemajuan bidang pendidikan", "kemajuan bidang pendidikan pembelajaran", "kemajuan bidang pendidikan pengajaran", "kemajuan bidang pendidikan proses", "meningkatkan bidang pembelajaran", "kemajuan pendidikan pembelajaran pengajaran", "kerajaan meningkatkan proses", "bidang proses pembelajaran", "kemajuan proses", "kemajuan pendidikan proses pengajaran", "kemajuan pendidikan pembelajaran", "bidang proses pembelajaran pengajaran", "bidang pembelajaran", "bidang proses", "proses pembelajaran pengajaran", "kerajaan meningkatkan bidang pembelajaran", "kerajaan meningkatkan bidang", "kerajaan meningkatkan", "kerajaan kemajuan proses pembelajaran", "kerajaan kemajuan proses", "kerajaan kemajuan pendidikan proses", "kerajaan kemajuan pendidikan pembelajaran", "kerajaan kemajuan pendidikan", "kerajaan kemajuan bidang pendidikan", "kerajaan kemajuan bidang proses", "kerajaan meningkatkan bidang proses", "kerajaan kemajuan bidang pembelajaran", "kerajaan kemajuan bidang", "kerajaan kemajuan", "kerajaan bidang proses pembelajaran", "kerajaan bidang proses", "kerajaan bidang pendidikan proses", "kerajaan meningkatkan bidang pendidikan", "kerajaan meningkatkan kemajuan bidang", "kerajaan meningkatkan kemajuan", "proses pembelajaran", "kerajaan bidang pendidikan pembelajaran", "awam", "mencapai", "pendidikan", "kerajaan", "proses pengajaran", "pelbagai", "asli", "isu", "pembelajaran pengajaran", "bidang pembelajaran pengajaran", "bidang pendidikan", "bidang pendidikan pembelajaran", "meningkatkan bidang", "bidang pendidikan pengajaran", "bidang pendidikan pembelajaran pengajaran", "kemajuan bidang proses pengajaran", "kemajuan pembelajaran", "kemajuan pembelajaran pengajaran", "bidang", "proses", "meningkatkan", "pembelajaran", "kerajaan meningkatkan kemajuan pembelajaran", "bahasa", "ilmu", "status", "sokongan", "bahasa ilmu", "allahyarham nik", "nik", "swasta", "ilmu bahasa", "inggeris", "bahasa inggeris", "bahasa bahasa", "bank", "status umno", "mca", "jawatan", "bon", "didakwa", "kalangan", "menyumbang", "allahyarham", "allahyarham aziz", "nik aziz", "allahyarham nik aziz", "guru nik aziz", "guru nik", "guru aziz", "guru", "aziz", "ilmu ilmu", "masyarakat", "pimpinan", "keluarga", "wang", "ahli", "syarikat", "dilaksanakan", "program", "kapal", "harga", "negara", "projek", "umno", "hutang", "hutang hutang", "tempoh hutang", "hutang diselesaikan", "pas parti", "kewangan hutang", "hutang pendek", "hutang mdb", "pelaburan", "hutang projek", "tumpuan", "membabitkan", "berita palsu", "palsu", "kelulusan", "harapan", "berita", "diselesaikan", "kewangan hutang hutang", "mewujudkan kewangan", "mdb hutang pendek", "diselesaikan tempoh", "mdb hutang", "pendek", "parti islam", "pas parti islam", "sebarang memusnahkan", "memusnahkan", "suasana", "mdb diselesaikan", "mdb", "islam", "kewangan", "mewujudkan", "mengundi", "pakatan harapan", "pengurusan", "majlis", "parti", "sumber", "pas", "lihat", "malaysia", "tempoh", "politik", "ros", "perlembagaan umno", "fasal perlembagaan umno", "umno pemilihan", "pekan", "parti perlembagaan", "melebihi", "pemilihan melebihi", "sumbangan", "bersatu", "perlembagaan", "penangguhan", "pemilihan umno", "pembangunan arus perdana", "pembangunan arus", "arus perdana", "arus", "pelopor", "pembangunan perdana", "idea", "kumpulan", "pertumbuhan pendapatan", "tangguh", "dikehendaki", "menyokong", "wanita", "usahawan", "usahawan wanita", "berkongsi pelbagai", "parti perlembagaan umno", "pemilihan", "umno", "saiful", "asli", "pelbagai", "pertumbuhan", "parti", "keputusan", "pendapatan", "meningkatkan", "malaysia", "najib", "perdana", "wujud", "berbeza", "pembangunan", "usaha", "diterima", "jakoa", "jho", "jho low", "tuntutan sivil doj", "sivil doj", "tuntutan doj", "tuntutan sivil", "low", "gembira projek", "gembira", "urusan perniagaan", "perniagaan jho", "perniagaan low", "berjalan", "gembira projek berjalan", "projek berjalan", "projek berjalan lancar", "gembira berjalan", "gembira berjalan lancar", "gembira lancar", "projek lancar", "gembira projek lancar", "gembira projek berjalan lancar", "bvi perniagaan", "bvi urusan jho low", "perniagaan jho low", "bvi urusan perniagaan", "bvi urusan", "bvi urusan perniagaan jho", "bvi urusan perniagaan low", "bvi", "sivil", "bvi perniagaan jho", "tuntutan", "doj", "lancar", "berjalan lancar", "urusan", "perniagaan", "nilai", "mdb", "projek", "bukti", "sebarang", "pilihan", "pilihan raya", "raya", "air", "kerja", "bertanding", "bersih", "air bersih", "berlaku jemaah menteri", "selesaikan", "jppm pendaftaran", "disediakan", "parti pru", "parti bertanding", "jppm pendaftaran ph", "pendaftaran ph", "kerusi", "membina", "terdekat", "peraturan", "bekalan", "bekalan air", "bekalan air bersih", "bekalan bersih", "berlaku jemaah", "berlaku menteri", "pencemaran", "ph keputusan", "bincang", "memandangkan", "ph", "jppm", "pendaftaran", "ambil", "berlaku", "jemaah menteri", "media", "parti", "rakyat", "perniagaan", "pru", "keputusan", "menteri", "malaysia", "buku", "positif", "terbaik", "dilaksanakan", "perkhidmatan"], "Total": [14.0, 25.0, 15.0, 10.0, 7.0, 15.0, 27.0, 7.0, 5.0, 11.0, 7.0, 4.0, 9.0, 7.0, 5.0, 4.0, 3.0, 6.0, 6.0, 3.0, 3.0, 3.0, 6.0, 6.0, 7.0, 4.0, 4.0, 5.0, 7.0, 3.0, 7.7554386247113, 7.7554386247113, 7.7554386247113, 7.7554386247113, 7.7554386247113, 7.7554386247113, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 4.208030871863507, 6.651035805724923, 27.109713794541875, 4.208030871863507, 4.208030871863507, 4.208030871863507, 8.451378283229499, 8.971849132378718, 25.551045649037505, 5.764184085142775, 5.764184085142775, 4.208030871863507, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.9537111492151413, 3.953705777798179, 3.953681757683694, 27.109713794541875, 4.840561765303099, 5.7217643941582645, 3.772920594695674, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948528238827543, 2.9948517509439427, 2.9948475325082287, 2.9948503147565195, 2.9948401619895386, 2.994839578748502, 2.216776316438863, 2.216776316438863, 4.434925623349494, 5.1045281938089, 11.136013443049729, 15.572615332139375, 27.109713794541875, 3.5842051084268185, 6.692484357725886, 3.656849034942385, 3.3086055854026397, 2.646609604486411, 2.6466096044806027, 2.6466096044612946, 2.6466096044572858, 2.646609604455687, 2.646609604455687, 2.6466096044099046, 2.646609497983717, 2.646609497983717, 2.646609497983717, 2.646609497983717, 2.6466099562548777, 2.6466099908362946, 2.646608937685223, 2.646608385595131, 2.64660882720987, 2.6466079531299562, 2.646606926638991, 6.379792963729857, 3.8110525927957286, 1.9846141093238363, 1.9846141093238363, 1.9846141093238363, 1.9846141093238363, 1.984614109309696, 1.984614109309696, 1.984614109309696, 1.984614109309696, 1.984614109309696, 14.348598357400698, 1.984614109309696, 3.9782067746008174, 5.211316893361838, 4.375736671633358, 3.1490479605331503, 4.480711043191374, 3.1938130747665436, 3.2359608504604593, 3.2359604052134414, 25.551045649037505, 4.697889815163333, 15.432130581840081, 27.109713794541875, 6.009547507791347, 11.136013443049729, 7.686363656117806, 4.976556663761384, 9.139740506786453, 8.478861580267067, 6.692484357725886, 7.004745506742573, 5.795203418730813, 5.224714206244648, 3.339029840401878, 2.6694285215031592, 2.6694278561147264, 2.6694278561147264, 2.6694294712706297, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 4.590377369577994, 3.258779304042449, 5.872410802661842, 15.432130581840081, 1.9998267206960656, 6.083103484259932, 7.381503898375387, 7.686363656117806, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 1.9998267206960656, 6.0820690215013045, 3.7366139635093982, 6.002406942272587, 2.589177602593873, 1.9998267206960656, 4.786077020679972, 3.01802534854937, 3.0180253485753226, 3.0180249672948523, 2.4286747911724627, 2.4286747911726203, 2.4286747911726203, 2.42867479117469, 2.4286747911748945, 2.4286747911749456, 2.4286747911749456, 2.4286747911773774, 2.428674791181176, 2.428674791205802, 2.428674791272594, 2.4286747913006037, 2.428676477041608, 2.428678719668682, 2.4286726223129893, 2.428679712777999, 1.8393242337979583, 1.8393242337979583, 1.8393242337979583, 1.8393242337979583, 1.8393242337979583, 1.8393242337979583, 1.8393242337979583, 1.8393242337979583, 1.8393242337979583, 1.8393242337986766, 6.603057811897336, 3.0114278513904926, 3.09827234752296, 4.748214729985793, 6.452435287995304, 7.8121778245874705, 4.015415296327241, 4.76706215819024, 4.898468570662687, 5.7217643941582645, 27.109713794541875, 9.139740506786453, 7.987159210824422, 7.070898497946941, 2.9916322416137775, 2.9916322416144587, 2.9916322416212617, 2.9916336650747986, 2.408879960970812, 2.4088799609752507, 2.4088799609878397, 2.408879982492345, 2.4088802537587184, 2.408879508955386, 2.4088797097762966, 2.4088824117379275, 2.4088824117379275, 4.139067122485152, 4.236381795490681, 3.4940812135011248, 4.352459699458817, 1.826127680328815, 1.8261276803329891, 1.826127680335962, 1.826127680335962, 1.826127680335962, 1.826127680335962, 1.8261276803383093, 1.8261276803383093, 1.8261276803449233, 1.8261276803449233, 1.8261276803525157, 1.8261276803660356, 10.023393530789754, 4.825885283704185, 5.220928783589308, 2.9113281200354324, 2.956081379448147, 3.0708749492086063, 3.0784796638821734, 3.186933128090762, 15.572615332139375, 5.3077282516887205, 5.487671357721618, 3.6605108504688255, 25.551045649037505, 4.207845270404587, 4.20784696095283, 5.196152569080346, 2.3546716032305586, 2.3546716032305586, 2.3546716032474757, 2.354670695142312, 2.354672993126908, 2.3546729931309756, 2.354672993130976, 2.354739219226797, 4.0667879113486975, 3.42180363232718, 1.7899880449064225, 1.7899880449064225, 1.7899880449066436, 1.7899880449066436, 1.7899880449066436, 1.7899880449066436, 1.7899880449066436, 1.7899880449066436, 1.7899880449321872, 1.7899880449754677, 1.7899880449754677, 1.7899880449829308, 1.789988045165487, 1.7899881037787293, 1.7899881037787277, 1.7899881037787277, 1.7899881037787277, 1.789988533964445, 1.789989808981343, 4.299015051435122, 7.987159210824422, 2.9374233748932705, 7.381503898375387, 6.083103484259932, 4.826095091847535, 15.572615332139375, 7.702216360913585, 5.795203418730813, 6.002406942272587, 25.551045649037505, 4.119239589398851, 8.478861580267067, 3.259573614511443, 3.042337604665398, 5.404383794650271, 3.115698452316275, 4.4087596145351915, 2.459588417988318, 4.495720864529139, 3.9605644955650727, 3.396635056086975, 3.3966350624811104, 2.849448682548078, 2.849448710823281, 5.158484054886342, 2.302227522417642, 2.302227522417642, 2.3022279351885575, 2.3022285856816533, 2.302228585681654, 3.961313603196771, 1.7550260546338656, 1.7550260546338656, 1.7550260546338656, 1.7550260546338656, 1.7550260546338656, 1.7550260546338656, 1.7550260546338656, 1.7550260546338656, 1.7550260546338656, 1.7550267192357356, 1.7550267192357356, 1.7550267192357356, 1.7550267192357356, 1.7550267192357356, 1.7550267192357356, 1.7550267192357356, 1.7550267192357356, 3.4387987850350705, 1.7550267192357356, 3.5190484602942878, 4.31878716632742, 2.8669099691069, 2.8669099691069, 2.9642214017634254, 7.004745506742573, 3.721057306830067, 10.023393530789754, 9.139740506786453, 2.3443782875820625, 3.509883038333451, 3.6753031647925494, 3.6753031647925494, 3.6753031647925494, 2.6704095562935, 2.670409972594208, 2.67040989398393, 2.167963018236399, 2.167963018236399, 2.167963064300581, 2.167963078000069, 2.167967323533607, 1.665516281230345, 1.665516281246435, 1.6655162812649222, 1.665516281291777, 1.665516281291777, 1.6655162813085025, 1.66551628146496, 1.6655162814809938, 1.665516281938916, 1.6655165323176382, 1.6655165323176382, 1.6655165323176382, 1.6655165323176382, 1.665516606505649, 1.665516606505649, 1.6655166280959064, 1.665517105923494, 1.6655171061244252, 1.6655194765287513, 4.302220398313717, 3.8359160658593305, 2.75071729493087, 2.757314019942572, 3.936669250740204, 2.946038298833293, 3.0436357361595996, 15.572615332139375, 14.348598357400698, 7.004745506742573, 3.3061347474781284, 7.702216360913585, 11.136013443049729, 25.551045649037505, 2.5523580836171087, 2.882316685931178, 2.916860395467091, 4.015415296327241, 2.7948842404952465], "loglift": [30.0, 29.0, 28.0, 27.0, 26.0, 25.0, 24.0, 23.0, 22.0, 21.0, 20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 1.1948, 1.1948, 1.1948, 1.1948, 1.1948, 1.1948, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 1.1254, 0.8858, -0.0567, 1.1254, 1.1254, 1.1254, 0.6463, 0.5865, -0.281, 0.8107, 0.8107, 1.1254, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 1.5736, 0.0272, 1.3713, 1.204, 1.8952, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.8465, 1.7579, 1.7579, 1.7335, 1.5929, 1.0254, 0.5582, -0.3564, 1.6669, 1.0425, 1.6468, 2.2645, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.2081, 2.157, 2.1231, 2.1065, 2.1065, 2.1065, 2.1065, 2.1065, 2.1065, 2.1065, 2.1065, 2.1065, 2.101, 2.1065, 2.0802, 1.9992, 1.9849, 2.0343, 1.9612, 2.0202, 2.0071, 2.0071, 1.5642, 1.9139, 1.6085, 1.2125, 1.7791, 1.4481, 1.627, 1.8563, 1.5136, 1.5417, 1.56, 1.5144, 1.6239, 1.528, 2.3504, 2.2947, 2.2947, 2.2947, 2.2947, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.0321, 2.0952, 1.7858, 1.217, 2.194, 1.471, 1.2775, 1.2371, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 2.194, 1.0817, 1.5689, 1.0949, 1.9357, 2.194, 2.7079, 2.6199, 2.6199, 2.6199, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5576, 2.5575, 2.4461, 2.4461, 2.4461, 2.4461, 2.4461, 2.4461, 2.4461, 2.4461, 2.4461, 2.4461, 2.2343, 2.3425, 2.3141, 2.1667, 2.0659, 1.8871, 2.0096, 1.8832, 1.856, 1.7006, 0.4246, 1.2323, 1.3671, 2.7566, 2.6208, 2.6208, 2.6208, 2.6208, 2.5579, 2.5579, 2.5579, 2.5579, 2.5579, 2.5579, 2.5579, 2.5579, 2.5579, 2.5144, 2.4912, 2.4655, 2.4641, 2.4454, 2.4454, 2.4454, 2.4454, 2.4454, 2.4454, 2.4454, 2.4454, 2.4454, 2.4454, 2.4454, 2.4454, 2.2968, 2.3562, 2.2822, 2.3684, 2.3532, 2.3151, 2.3126, 2.278, 1.7684, 2.0475, 2.0141, 2.1255, 0.8687, 2.0001, 2.0001, 2.7115, 2.6744, 2.6744, 2.6744, 2.6744, 2.6744, 2.6744, 2.6744, 2.6742, 2.6258, 2.5802, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5591, 2.5357, 2.2484, 2.4532, 2.2087, 2.2158, 2.2363, 1.4944, 1.7476, 1.8707, 1.7386, 0.2901, 1.7367, 1.0148, 1.9597, 2.0287, 1.4541, 2.0049, 1.6577, 2.2413, 2.9709, 2.9382, 2.9227, 2.9227, 2.8801, 2.8801, 2.8324, 2.8138, 2.8138, 2.8138, 2.8138, 2.8138, 2.7689, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6957, 2.6921, 2.6957, 2.6691, 2.6097, 2.5945, 2.5945, 2.5611, 1.9807, 2.285, 1.6185, 1.5069, 2.4062, 2.0026, 3.0352, 3.0352, 3.0352, 2.9573, 2.9573, 2.9573, 2.8861, 2.8861, 2.8861, 2.8861, 2.8861, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.7603, 2.6986, 2.5951, 2.6481, 2.6457, 2.5484, 2.5795, 2.4927, 1.2993, 1.2759, 1.7133, 2.2541, 1.6185, 1.2498, 0.2379, 2.3335, 2.2119, 2.2, 1.8803, 2.2427], "logprob": [30.0, 29.0, 28.0, 27.0, 26.0, 25.0, 24.0, 23.0, 22.0, 21.0, 20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, -5.3053, -5.3053, -5.3053, -5.3053, -5.3053, -5.3053, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.9861, -5.7679, -5.3053, -5.9861, -5.9861, -5.9861, -5.7679, -5.7679, -5.5889, -5.9861, -5.9861, -5.9861, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.6002, -5.2214, -5.6002, -5.6002, -5.3255, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.6051, -5.9945, -5.9945, -5.3255, -5.3255, -5.1129, -5.2448, -5.605, -5.6051, -5.6051, -5.6051, -5.0875, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -5.3671, -4.5384, -5.0875, -5.7566, -5.7566, -5.7566, -5.7566, -5.7566, -5.7566, -5.7566, -5.7566, -5.7566, -3.7838, -5.7566, -5.0875, -4.8985, -5.0875, -5.3671, -5.0875, -5.3671, -5.3671, -5.3671, -3.7437, -5.0875, -4.2035, -4.0361, -4.976, -4.6902, -4.8821, -5.0875, -4.8223, -4.8693, -5.0875, -5.0875, -5.1676, -5.3671, -4.9924, -5.272, -5.272, -5.272, -5.272, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -4.9924, -5.272, -4.9924, -4.5951, -5.6614, -5.272, -5.272, -5.272, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -5.6614, -4.2749, -4.824, -4.824, -4.824, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.1036, -5.493, -5.493, -5.493, -5.493, -5.493, -5.493, -5.493, -5.493, -5.493, -5.493, -4.4267, -5.1036, -5.1036, -4.824, -4.6182, -4.6057, -5.1488, -5.1036, -5.1036, -5.1036, -4.824, -5.1036, -5.1036, -3.8359, -4.8319, -4.8319, -4.8319, -4.8319, -5.1115, -5.1115, -5.1115, -5.1115, -5.1115, -5.1115, -5.1115, -5.1115, -5.1115, -4.6136, -4.6136, -4.8319, -4.6136, -5.5009, -5.5009, -5.5009, -5.5009, -5.5009, -5.5009, -5.5009, -5.5009, -5.5009, -5.5009, -5.5009, -5.5009, -3.9468, -4.6183, -4.6136, -5.1115, -5.1115, -5.1115, -5.1115, -5.1115, -4.0346, -4.8319, -4.8319, -5.1254, -4.4391, -5.1115, -5.1115, -4.189, -5.0177, -5.0177, -5.0177, -5.0177, -5.0177, -5.0177, -5.0177, -5.0178, -4.5199, -4.7381, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -4.5544, -4.2223, -5.0177, -4.3408, -4.5272, -4.7381, -4.3085, -4.7594, -4.9208, -5.0177, -5.0177, -5.3962, -5.3961, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -5.4072, -4.0745, -4.2339, -4.403, -4.403, -4.6212, -4.6212, -4.0755, -4.9008, -4.9008, -4.9008, -4.9008, -4.9008, -4.403, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -5.2903, -4.6212, -5.2903, -4.6212, -4.4758, -4.9008, -4.9008, -4.9008, -4.6212, -4.9495, -4.625, -4.829, -5.2903, -5.2903, -4.2117, -4.2117, -4.2117, -4.609, -4.609, -4.609, -4.8886, -4.8886, -4.8886, -4.8886, -4.8886, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -5.278, -4.3907, -4.609, -4.8886, -4.8886, -4.6297, -4.8886, -4.9427, -4.5036, -4.609, -4.8886, -5.0986, -4.8885, -4.8886, -5.0699, -5.278, -5.278, -5.278, -5.278, -5.278]}, "token.table": {"Topic": [5, 6, 7, 10, 10, 10, 6, 6, 6, 6, 6, 10, 4, 8, 8, 4, 5, 8, 4, 5, 6, 6, 6, 6, 6, 6, 6, 10, 10, 10, 10, 5, 7, 8, 7, 10, 7, 8, 9, 8, 9, 1, 3, 4, 8, 8, 1, 1, 1, 3, 1, 1, 1, 1, 5, 6, 10, 10, 10, 10, 7, 8, 10, 10, 1, 2, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 6, 6, 9, 1, 10, 9, 9, 9, 9, 9, 9, 9, 9, 4, 6, 7, 6, 8, 6, 7, 10, 10, 3, 7, 7, 3, 4, 6, 8, 2, 9, 8, 4, 9, 9, 9, 9, 9, 9, 9, 9, 6, 6, 6, 6, 4, 4, 7, 2, 6, 7, 7, 7, 7, 7, 7, 8, 6, 6, 6, 6, 4, 6, 7, 4, 5, 7, 8, 5, 8, 6, 3, 10, 9, 9, 7, 10, 10, 10, 6, 2, 6, 5, 3, 6, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 4, 10, 4, 10, 2, 4, 6, 7, 4, 10, 4, 3, 4, 6, 7, 8, 10, 3, 3, 4, 5, 6, 7, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 1, 1, 1, 1, 2, 7, 7, 7, 8, 2, 8, 9, 2, 5, 4, 6, 7, 4, 9, 3, 7, 1, 3, 4, 6, 7, 8, 10, 1, 3, 1, 1, 1, 1, 3, 1, 1, 4, 4, 1, 1, 1, 1, 1, 5, 6, 8, 10, 6, 4, 5, 7, 9, 7, 7, 7, 2, 10, 4, 8, 3, 3, 10, 7, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 9, 4, 10, 4, 7, 3, 5, 6, 2, 4, 7, 8, 7, 9, 2, 4, 5, 8, 5, 5, 5, 4, 3, 4, 8, 9, 10, 3, 3, 3, 3, 4, 3, 3, 3, 8, 6, 7, 10, 7, 3, 8, 3, 1, 2, 3, 4, 5, 6, 7, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 4, 5, 4, 6, 6, 6, 2, 6, 9, 4, 7, 7, 3, 7, 8, 9, 10, 10, 7, 8, 8, 10, 4, 5, 7, 10, 7, 7, 8, 7, 5, 6, 8, 8, 1, 4, 6, 8, 8, 8, 8, 1, 1, 1, 1, 1, 5, 6, 5, 3, 8, 8, 3, 8, 8, 10, 7, 10, 10, 2, 4, 8, 7, 1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 1, 3, 6, 7, 8, 1, 1, 1, 1, 1, 1, 1, 5, 7, 4, 6, 10, 3, 4, 8, 9, 10, 3, 4, 9, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 8, 10, 8, 10, 8, 4, 9, 10, 9, 9, 9, 4, 4, 4, 4, 4, 4, 4, 4, 7, 8, 8, 4, 4, 8, 10, 10, 10, 10, 6, 7, 5, 7, 8, 5, 9, 10, 1, 6, 8, 1, 4, 6, 7, 9, 9, 9, 9, 5, 6, 7, 8, 5, 5, 5, 8, 9, 10, 4, 7, 10, 4, 4, 7, 10, 4, 4, 10, 3, 7, 8, 4, 8, 10, 7, 8, 6, 7, 9, 7, 1, 10, 3, 4, 5, 3, 3, 3, 4, 6, 9, 9, 6, 6, 6, 7, 8, 2, 5, 7, 6, 2, 4, 5, 6, 8, 8, 1, 1, 1, 5, 7, 8, 7, 4, 4, 6, 10, 10, 5, 5, 4, 5, 7, 7, 5, 9, 9, 9, 9, 3, 6, 8, 8, 4, 7, 10, 4, 9, 9, 2, 8, 10, 8, 8, 6, 7, 8, 8, 1, 7, 8], "Freq": [0.1549802447241107, 0.4649407341723321, 0.1549802447241107, 0.1549802447241107, 0.7489487877567285, 0.9225249615313853, 0.5436779343330533, 0.5436779343330533, 0.8234943629625907, 0.5436779343330533, 0.36267178593638294, 0.7253435718727659, 0.7556837988751747, 0.5586629490881068, 0.5586629490881068, 0.13547374813689286, 0.2709474962737857, 0.4064212444106786, 0.2178470133256022, 0.6535410399768066, 0.2178470133256022, 0.5436779343330533, 0.8357575489731062, 0.8234943629609778, 0.8234943629626442, 0.8234943629618023, 0.8234943629596897, 0.6004143342897094, 0.6004143342897094, 0.6004143342897094, 0.6004143342897094, 0.32869461905427877, 0.32869461905427877, 0.32869461905427877, 0.5723965408336826, 0.2861982704168413, 0.830260535032537, 0.25244151313670354, 0.7573245394101106, 0.34880760497390856, 0.6976152099478171, 0.591619477017347, 0.23664779080693882, 0.11832389540346941, 0.11832389540346941, 0.5586627964511103, 0.9505633684261966, 0.902592404986066, 0.7517626045098446, 0.3007050418039378, 0.9505633684261966, 0.902592404986066, 0.9505633684261966, 0.9505633684261966, 0.25402184849844117, 0.25402184849844117, 0.5080436969968823, 0.6004143075451276, 0.9225249419298716, 0.6004143075451276, 0.24589430818593216, 0.7376829245577965, 0.9225249615313853, 0.7489486930473587, 0.3288354658471662, 0.3288354658471662, 0.1644177329235831, 0.1644177329235831, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.6004141274339414, 0.8234937913328899, 0.42655232105539453, 0.42655232105539453, 0.3917945551679161, 0.3917945551679161, 0.569791894926518, 0.569791894926518, 0.569791894926518, 0.569791894926518, 0.569791894926518, 0.569791894926518, 0.569791894926518, 0.569791894926518, 0.6695365916440035, 0.22317886388133448, 0.22317886388133448, 0.82349303092376, 0.5586629490073206, 0.49808048543056793, 0.24904024271528397, 0.24904024271528397, 0.6004144248060326, 0.22975514285045295, 0.6892654285513589, 0.5476068353643404, 0.22682116682050682, 0.22682116682050682, 0.22682116682050682, 0.22682116682050682, 0.23154648781879497, 0.6946394634563849, 0.8493753427255177, 0.7556845634572046, 0.8687238687424503, 0.5697921106981061, 0.5697921106981061, 0.5697921106981061, 0.8687238687424503, 0.5697921106981061, 0.5697921106981061, 0.5697921106981061, 0.5436779343330533, 0.5436779343330533, 0.5436779343330533, 0.5436779343330533, 0.7556842703637845, 0.23605049031804143, 0.7081514709541243, 0.5243137943713485, 0.34954252958089904, 0.8485484555805913, 0.6685313696566312, 0.6685313696583037, 0.8302613797243076, 0.8302613797286466, 0.8302612788158654, 0.5586629490801345, 0.6626849575538889, 0.8234943629618197, 0.5436779343328411, 0.8234943629618023, 0.2072158663565318, 0.2072158663565318, 0.6216475990695954, 0.39030159568526407, 0.26020106379017605, 0.13010053189508802, 0.13010053189508802, 0.40657208851954746, 0.40657208851954746, 0.8234943629191952, 0.33943890016502015, 0.6788778003300403, 0.8897349547565696, 0.757467781009327, 0.2606939210428156, 0.5213878420856312, 0.9225231295184679, 0.6004144247838865, 0.8234950983616988, 0.6124363067198666, 0.40829087114657775, 0.7492242187473614, 0.5580037803355069, 0.27900189016775345, 0.6678126886813757, 0.7951399783546151, 0.755683829262939, 0.755683829262939, 0.755683829262939, 0.755683829262939, 0.3227605219403939, 0.6455210438807878, 0.724801002550246, 0.24160033418341537, 0.749224031993858, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.21286152705674571, 0.6385845811702372, 0.21286152705674571, 0.6351125880157727, 0.3175562940078864, 0.1913980287773036, 0.3827960575546072, 0.1913980287773036, 0.1913980287773036, 0.7871840986060092, 0.2623946995353364, 0.7556837988533299, 0.1298327589282868, 0.1298327589282868, 0.1298327589282868, 0.1298327589282868, 0.2596655178565736, 0.2596655178565736, 0.6678136293385762, 0.06479986640190567, 0.45359906481333967, 0.2591994656076227, 0.06479986640190567, 0.06479986640190567, 0.06479986640190567, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.7489486710001578, 0.600414424777857, 0.9505633684261966, 0.9505633684261966, 0.9505633684261966, 0.9505633684261966, 0.383073602973958, 0.574610404460937, 0.8302613797301764, 0.5476068353664837, 0.5586629490666265, 0.7587818033517663, 0.34880760497390856, 0.6976152099478171, 0.7587864132386775, 0.7492237654243077, 0.2731859133464728, 0.2731859133464728, 0.5463718266929456, 0.19385540196693177, 0.7754216078677271, 0.31378129374151104, 0.6275625874830221, 0.19568670764706445, 0.07827468305882578, 0.3913734152941289, 0.03913734152941289, 0.15654936611765155, 0.07827468305882578, 0.03913734152941289, 0.6939403636171212, 0.3469701818085606, 0.9505633684261966, 0.9505633684261966, 0.9505633684261966, 0.6939403636171212, 0.3469701818085606, 0.9505633684261966, 0.9505633684261966, 0.5038762927774926, 0.5038762927774926, 0.9505633684261966, 0.9505633684261966, 0.9505633684261966, 0.9505633684261966, 0.9505633684261966, 0.151444986321066, 0.605779945284264, 0.151444986321066, 0.151444986321066, 0.8234943629286925, 0.09976661067214518, 0.09976661067214518, 0.598599664032871, 0.19953322134429036, 0.5476068353553222, 0.5476068353643404, 0.5476068353643404, 0.32855442854728095, 0.32855442854728095, 0.75568402078839, 0.8493748413619966, 0.9022110102713913, 0.9022110102713913, 0.6004132729112144, 0.8302614663086403, 0.6678130089325013, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.6262107246668445, 0.31310536233342223, 0.7556841468823008, 0.6004144247214545, 0.755683698413244, 0.5476068353616531, 0.6678152728763179, 0.6137267404144371, 0.30686337020721854, 0.16640187945989365, 0.4992056383796809, 0.16640187945989365, 0.16640187945989365, 0.6765713602828377, 0.33828568014141885, 0.3331996679390043, 0.16659983396950215, 0.16659983396950215, 0.3331996679390043, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.7556839892444556, 0.35919496868931156, 0.35919496868931156, 0.08979874217232789, 0.08979874217232789, 0.17959748434465578, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.676448773843075, 0.22548292461435834, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.5586629307138768, 0.8234926941899383, 0.6869716904241144, 0.3434858452120572, 0.5476068353652319, 0.4855265047333345, 0.24276325236666724, 0.6678124494301688, 0.25821002955071193, 0.18443573539336566, 0.07377429415734627, 0.29509717662938506, 0.03688714707867313, 0.07377429415734627, 0.07377429415734627, 0.2065875922022004, 0.6197627766066013, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.9505633684261966, 0.7587807724890413, 0.7587807724890413, 0.7587807724890413, 0.902592404986066, 0.9505633684261966, 0.7541086147542009, 0.2513695382514003, 0.618054533911419, 0.3090272669557095, 0.8234943629625907, 0.5436779343330533, 0.2687408221755903, 0.2687408221755903, 0.5374816443511806, 0.3256400916806168, 0.6512801833612336, 0.830260535032537, 0.192645868148331, 0.32107644691388504, 0.256861157531108, 0.064215289382777, 0.128430578765554, 0.6004144247935675, 0.5476068353636365, 0.8493748413634638, 0.5586623985133665, 0.6004144248002322, 0.1822266558643158, 0.1822266558643158, 0.3644533117286316, 0.1822266558643158, 0.6685310515617543, 0.5476068353636365, 0.8493756702905428, 0.8302613723124147, 0.3287795456998245, 0.16438977284991224, 0.4931693185497368, 0.5586629490881068, 0.37006994247517616, 0.18503497123758808, 0.18503497123758808, 0.18503497123758808, 0.5586629490881068, 0.5586629490881068, 0.5586629490881068, 0.9505633684261966, 0.9505633684261966, 0.902592404986066, 0.9505633684261966, 0.9505633684261966, 0.38622302270735953, 0.38622302270735953, 0.5000433235795234, 0.2326114209965779, 0.6978342629897336, 0.8493748413619964, 0.6678154029324568, 0.5586629490881758, 0.5586629490881758, 0.6004142997618973, 0.3635415394533053, 0.7270830789066106, 0.6004144247838865, 0.1725564967690136, 0.5176694903070408, 0.3451129935380272, 0.5476068353643404, 0.1702878142562371, 0.3405756285124742, 0.5108634427687113, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.7556836885392494, 0.5000433235795234, 0.5572987158193936, 0.22291948632775743, 0.11145974316387872, 0.11145974316387872, 0.11145974316387872, 0.9505633684261966, 0.9505633684261966, 0.902592404986066, 0.9505633684261966, 0.9505633684261966, 0.902592404986066, 0.9505633684261966, 0.32483566863616425, 0.6496713372723285, 0.6180544488711632, 0.3090272244355816, 0.6004144245505946, 0.23588072302708876, 0.35382108454063316, 0.11794036151354438, 0.11794036151354438, 0.11794036151354438, 0.2988426857794857, 0.44826402866922854, 0.14942134288974285, 0.14942134288974285, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.5469189405658664, 0.2734594702829332, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.35779657186188235, 0.35779657186188235, 0.5844870760861848, 0.2922435380430924, 0.8493753427255177, 0.4282810841753328, 0.28552072278355517, 0.28552072278355517, 0.8687234675299768, 0.569791894926518, 0.8687234675299765, 0.7556837988605014, 0.5038762927810827, 0.5038762927810827, 0.5038762927810827, 0.5038762927810827, 0.5038762927810827, 0.5038762927810827, 0.20720685791899265, 0.20720685791899265, 0.4144137158379853, 0.5586629490666265, 0.7556837988621025, 0.7556837988621025, 0.23243811507005926, 0.6973143452101778, 0.6004141275063766, 0.8162591942722999, 0.8162591942722999, 0.6641367811872108, 0.3320683905936054, 0.2376512285925814, 0.4753024571851628, 0.2376512285925814, 0.34694313948258404, 0.34694313948258404, 0.34694313948258404, 0.41954560977641564, 0.41954560977641564, 0.20977280488820782, 0.9505633684261966, 0.43764918676081827, 0.21882459338040913, 0.21882459338040913, 0.21882459338040913, 0.5697921106981061, 0.5697921106981061, 0.5697921106981061, 0.2676219726644729, 0.2676219726644729, 0.2676219726644729, 0.2676219726644729, 0.5000433235795234, 0.5000433235795234, 0.5000433235795234, 0.30246801064680906, 0.30246801064680906, 0.30246801064680906, 0.696932184657759, 0.13938643693155178, 0.13938643693155178, 0.7556837988549884, 0.7837244920682849, 0.156744898413657, 0.156744898413657, 0.5038762927774926, 0.5038762927774926, 0.8162591942722999, 0.6678124494301688, 0.19245008430862673, 0.7698003372345069, 0.6855988431498031, 0.22853294771660104, 0.22853294771660104, 0.3404344121951213, 0.6808688243902427, 0.2849097787813511, 0.2849097787813511, 0.2849097787813511, 0.5476068353616531, 0.9505633684261966, 0.9225249361003816, 0.5877134744085836, 0.19590449146952785, 0.19590449146952785, 0.6678124494301688, 0.6678124494301688, 0.6678124494301688, 0.9067263904878272, 0.29079921871317094, 0.5815984374263419, 0.883227059962284, 0.6626850412681181, 0.6626849575481903, 0.8234943629513397, 0.5476068353593764, 0.8493509530353517, 0.37680904243047386, 0.18840452121523693, 0.37680904243047386, 0.8234943629618888, 0.25601055747929186, 0.12800527873964593, 0.12800527873964593, 0.3840158362189378, 0.12800527873964593, 0.5586629490642971, 0.9505633684261966, 0.9505633684261966, 0.9505633684261966, 0.23765132407158343, 0.47530264814316686, 0.23765132407158343, 0.6685313696581514, 0.7556837988616459, 0.34283437135148365, 0.34283437135148365, 0.34283437135148365, 0.6004144247156743, 0.8984645670728498, 0.7492242187473614, 0.575670231035344, 0.19189007701178132, 0.19189007701178132, 0.8302615355249972, 0.28416772638486854, 0.5683354527697371, 0.7018901629109282, 0.7018901559460416, 0.8832270616249511, 0.2504019197826361, 0.2504019197826361, 0.5008038395652722, 0.8493753427194154, 0.6028264526445758, 0.20094215088152526, 0.20094215088152526, 0.3373567168110643, 0.6747134336221287, 0.8687237129872615, 0.3209553219941998, 0.3209553219941998, 0.3209553219941998, 0.5586629307138773, 0.5586629307138773, 0.42121094216098864, 0.21060547108049432, 0.21060547108049432, 0.5586629307138773, 0.3067885920870309, 0.3067885920870309, 0.3067885920870309], "Term": ["ahli", "ahli", "ahli", "ahli", "air", "air bersih", "allahyarham", "allahyarham aziz", "allahyarham nik", "allahyarham nik aziz", "ambil", "ambil", "anti", "arus", "arus perdana", "asli", "asli", "asli", "awam", "awam", "awam", "aziz", "bahasa", "bahasa bahasa", "bahasa ilmu", "bahasa inggeris", "bank", "bekalan", "bekalan air", "bekalan air bersih", "bekalan bersih", "berbeza", "berbeza", "berbeza", "berita", "berita", "berita palsu", "berjalan", "berjalan", "berjalan lancar", "berjalan lancar", "berkongsi", "berkongsi", "berkongsi", "berkongsi", "berkongsi pelbagai", "berkongsi pembangunannya negara", "berkongsi pembangunannya negara selatan", "berkongsi pengalaman", "berkongsi pengalaman", "berkongsi pengalaman negara", "berkongsi pengalaman negara selatan", "berkongsi pengalaman pembangunannya negara", "berkongsi pengalaman pembangunannya selatan", "berlaku", "berlaku", "berlaku", "berlaku jemaah", "berlaku jemaah menteri", "berlaku menteri", "bersatu", "bersatu", "bersih", "bertanding", "bidang", "bidang", "bidang", "bidang", "bidang pembelajaran", "bidang pembelajaran pengajaran", "bidang pendidikan", "bidang pendidikan pembelajaran", "bidang pendidikan pembelajaran pengajaran", "bidang pendidikan pengajaran", "bidang pendidikan proses pengajaran", "bidang pengajaran", "bidang proses", "bidang proses pembelajaran", "bidang proses pembelajaran pengajaran", "bincang", "bon", "bukti", "bukti", "buku", "buku", "bvi", "bvi perniagaan", "bvi perniagaan jho", "bvi urusan", "bvi urusan jho low", "bvi urusan perniagaan", "bvi urusan perniagaan jho", "bvi urusan perniagaan low", "cina", "cina", "cina", "didakwa", "dikehendaki", "dilaksanakan", "dilaksanakan", "dilaksanakan", "disediakan", "diselesaikan", "diselesaikan", "diselesaikan tempoh", "diterima", "diterima", "diterima", "diterima", "doj", "doj", "fasal perlembagaan umno", "gaji", "gembira", "gembira berjalan", "gembira berjalan lancar", "gembira lancar", "gembira projek", "gembira projek berjalan", "gembira projek berjalan lancar", "gembira projek lancar", "guru", "guru aziz", "guru nik", "guru nik aziz", "hak", "harapan", "harapan", "harga", "harga", "hutang", "hutang diselesaikan", "hutang hutang", "hutang mdb", "hutang pendek", "hutang projek", "idea", "ilmu", "ilmu bahasa", "ilmu ilmu", "inggeris", "islam", "islam", "islam", "isu", "isu", "isu", "isu", "jakoa", "jakoa", "jawatan", "jemaah menteri", "jemaah menteri", "jho", "jho low", "jppm", "jppm", "jppm pendaftaran", "jppm pendaftaran ph", "kalangan", "kapal", "kapal", "kasih", "kawasan", "kawasan", "kawasan bandar", "kebenaran", "kegiatan", "kegiatan kehidupan", "kegiatan kehidupan penduduk", "kegiatan penduduk", "keluarga", "keluarga", "kelulusan", "kelulusan", "kemajuan", "kemajuan bidang pembelajaran", "kemajuan bidang pembelajaran pengajaran", "kemajuan bidang pendidikan", "kemajuan bidang pendidikan pembelajaran", "kemajuan bidang pendidikan pengajaran", "kemajuan bidang pendidikan proses", "kemajuan bidang proses pengajaran", "kemajuan pembelajaran", "kemajuan pembelajaran pengajaran", "kemajuan pendidikan pembelajaran", "kemajuan pendidikan pembelajaran pengajaran", "kemajuan pendidikan pengajaran", "kemajuan pendidikan proses", "kemajuan pendidikan proses pembelajaran", "kemajuan pendidikan proses pengajaran", "kemajuan proses", "kemajuan proses pembelajaran", "kementerian", "kementerian", "kementerian", "kemudahan", "kemudahan", "kenyataan", "kenyataan", "kenyataan", "kenyataan", "kepimpinan", "kepimpinan", "kepimpinan negara", "keputusan", "keputusan", "keputusan", "keputusan", "keputusan", "keputusan", "keputusan umno", "kerajaan", "kerajaan", "kerajaan", "kerajaan", "kerajaan", "kerajaan", "kerajaan bidang pendidikan pembelajaran", "kerajaan bidang pendidikan proses", "kerajaan bidang proses", "kerajaan bidang proses pembelajaran", "kerajaan kemajuan", "kerajaan kemajuan bidang", "kerajaan kemajuan bidang pembelajaran", "kerajaan kemajuan bidang pendidikan", "kerajaan kemajuan bidang proses", "kerajaan kemajuan pendidikan", "kerajaan kemajuan pendidikan pembelajaran", "kerajaan kemajuan pendidikan proses", "kerajaan kemajuan proses", "kerajaan kemajuan proses pembelajaran", "kerajaan meningkatkan", "kerajaan meningkatkan bidang", "kerajaan meningkatkan bidang pembelajaran", "kerajaan meningkatkan bidang pendidikan", "kerajaan meningkatkan bidang proses", "kerajaan meningkatkan kemajuan", "kerajaan meningkatkan kemajuan bidang", "kerajaan meningkatkan kemajuan pembelajaran", "kerajaan meningkatkan proses", "kerajaan meningkatkan proses pembelajaran", "kerajaan pendidikan", "kerajaan pendidikan proses", "kerajaan pendidikan proses pembelajaran", "kerja", "kerusi", "kesediaan malaysia berkongsi negara", "kesediaan malaysia pembangunannya negara", "kesediaan malaysia pengalaman negara", "kesediaan pengalaman pembangunannya negara", "kewangan", "kewangan", "kewangan hutang", "kewangan hutang hutang", "kumpulan", "kwsp", "lancar", "lancar", "langkah", "laporan", "lihat", "lihat", "lihat", "low", "low", "majlis", "majlis", "malaysia", "malaysia", "malaysia", "malaysia", "malaysia", "malaysia", "malaysia", "malaysia berkongsi", "malaysia berkongsi", "malaysia berkongsi negara", "malaysia berkongsi negara selatan", "malaysia berkongsi pembangunannya negara", "malaysia berkongsi pengalaman", "malaysia berkongsi pengalaman", "malaysia berkongsi pengalaman negara", "malaysia berkongsi pengalaman pembangunannya", "malaysia kepimpinan", "malaysia kepimpinan negara", "malaysia pembangunannya negara", "malaysia pembangunannya negara selatan", "malaysia pengalaman negara", "malaysia pengalaman negara selatan", "malaysia pengalaman pembangunannya negara", "masyarakat", "masyarakat", "masyarakat", "masyarakat", "mca", "mdb", "mdb", "mdb", "mdb", "mdb diselesaikan", "mdb hutang", "mdb hutang pendek", "media", "media", "melayu", "melebihi", "memainkan peranan membangunkan kawasan", "memainkan peranan pengalaman", "memandangkan", "membabitkan", "membangunkan", "membantu negara", "membantu negara bidang", "membantu negara bidang ekonomi", "membantu negara bidang perancangan", "membantu negara maju", "membantu negara maju bidang", "membantu negara maju ekonomi", "membantu negara maju perancangan", "membantu negara perancangan", "membantu negara perancangan ekonomi", "membayar", "membayar", "membentuk", "membina", "memilih", "memusnahkan", "menangguhkan", "mencapai", "mencapai", "mengambil", "mengambil", "mengambil", "mengambil", "mengundi", "mengundi", "meningkatkan", "meningkatkan", "meningkatkan", "meningkatkan", "meningkatkan bidang", "meningkatkan bidang pembelajaran", "meningkatkan bidang pembelajaran pengajaran", "menjadikan", "menteri", "menteri", "menteri", "menteri", "menteri", "menteri najib", "menteri najib razak", "menteri razak", "menteri seri", "menteri seri", "menteri seri najib", "menteri seri najib razak", "menteri seri razak", "menyokong", "menyumbang", "mewujudkan", "mewujudkan", "mewujudkan kewangan", "najib", "najib", "najib razak", "negara", "negara", "negara", "negara", "negara", "negara", "negara", "negara bidang", "negara bidang", "negara bidang ekonomi", "negara bidang ekonomi kewangan", "negara bidang perancangan", "negara bidang perancangan ekonomi", "negara bidang perancangan kewangan", "negara maju", "negara maju bidang", "negara maju bidang ekonomi", "negara maju bidang kewangan", "negara maju bidang perancangan", "negara maju ekonomi", "negara maju ekonomi kewangan", "negara maju perancangan", "negara maju perancangan ekonomi", "negara maju perancangan kewangan", "negara negara selatan", "negara perancangan", "negara perancangan ekonomi", "negara perancangan ekonomi kewangan", "negara selatan", "negara selatan selatan", "negeri", "negeri", "nhrap", "nhrap", "nik", "nik aziz", "nilai", "nilai", "nilai", "pakatan harapan", "pakatan harapan", "palsu", "parti", "parti", "parti", "parti", "parti", "parti bertanding", "parti islam", "parti perlembagaan", "parti perlembagaan umno", "parti pru", "pas", "pas", "pas", "pas", "pas parti", "pas parti islam", "pekan", "pelaburan", "pelbagai", "pelbagai", "pelbagai", "pelopor", "pembangunan", "pembangunan", "pembangunan", "pembangunan", "pembangunan arus", "pembangunan arus perdana", "pembangunan perdana", "pembangunannya negara", "pembangunannya negara negara selatan", "pembangunannya negara selatan", "pembangunannya negara selatan selatan", "pembangunannya selatan", "pembelajaran", "pembelajaran", "pembelajaran pengajaran", "pemilihan", "pemilihan", "pemilihan melebihi", "pemilihan parti", "pemilihan umno", "penangguhan", "pencemaran", "pendaftaran", "pendaftaran", "pendaftaran ph", "pendapatan", "pendapatan", "pendapatan", "pendek", "pendidikan", "pendidikan", "pendidikan", "pendidikan pembelajaran", "pendidikan pembelajaran pengajaran", "pendidikan pengajaran", "pendidikan proses", "pendidikan proses pembelajaran", "pendidikan proses pembelajaran pengajaran", "pendidikan proses pengajaran", "penduduk", "pengajaran", "pengalaman", "pengalaman", "pengalaman", "pengalaman", "pengalaman", "pengalaman negara", "pengalaman negara negara selatan", "pengalaman negara selatan", "pengalaman negara selatan selatan", "pengalaman pembangunannya negara", "pengalaman pembangunannya negara selatan", "pengalaman pembangunannya selatan", "pengurusan", "pengurusan", "penjelasan", "penjelasan", "peraturan", "perdana", "perdana", "perdana", "perdana", "perdana", "perdana menteri", "perdana menteri", "perdana menteri", "perdana menteri", "perdana menteri najib", "perdana menteri najib razak", "perdana menteri razak", "perdana menteri seri", "perdana menteri seri najib", "perdana menteri seri razak", "perdana najib", "perdana najib razak", "perdana razak", "perdana seri", "perdana seri", "perdana seri najib", "perdana seri najib razak", "perdana seri razak", "perkhidmatan", "perkhidmatan", "perlembagaan", "perlembagaan", "perlembagaan umno", "perniagaan", "perniagaan", "perniagaan", "perniagaan jho", "perniagaan jho low", "perniagaan low", "pertimbangan", "pertimbangan kenyataan", "pertimbangan menulis kenyataan", "pertimbangan sewajarnya", "pertimbangan sewajarnya kenyataan", "pertimbangan sewajarnya menulis", "pertimbangan sewajarnya menulis kenyataan", "pertumbuhan", "pertumbuhan", "pertumbuhan", "pertumbuhan pendapatan", "pesara", "pesara tentera", "ph", "ph", "ph keputusan", "pilihan", "pilihan raya", "pimpinan", "pimpinan", "politik", "politik", "politik", "positif", "positif", "positif", "program", "program", "program", "program kerjasama teknikal malaysia", "projek", "projek", "projek", "projek", "projek berjalan", "projek berjalan lancar", "projek lancar", "proses", "proses", "proses", "proses", "proses pembelajaran", "proses pembelajaran pengajaran", "proses pengajaran", "pru", "pru", "pru", "rakyat", "rakyat", "rakyat", "rakyat kepimpinan", "rakyat malaysia", "rakyat malaysia", "rakyat malaysia", "rakyat malaysia kepimpinan", "rakyat malaysia kepimpinan negara", "raya", "razak", "ros", "ros", "rumah", "rumah", "rumah", "saiful", "saiful", "sebarang", "sebarang", "sebarang", "sebarang memusnahkan", "selatan", "selesaikan", "seri", "seri", "seri", "seri najib", "seri najib razak", "seri razak", "serius", "sivil", "sivil", "sivil doj", "sokongan", "status", "status umno", "suasana", "sumbangan", "sumber", "sumber", "sumber", "swasta", "syarikat", "syarikat", "syarikat", "syarikat", "syarikat", "tangguh", "teknikal malaysia", "teknikal malaysia berkongsi", "teknikal malaysia berkongsi pengalaman", "tempoh", "tempoh", "tempoh", "tempoh hutang", "tentera", "terbaik", "terbaik", "terbaik", "terdekat", "terima", "terima kasih", "tindakan", "tindakan", "tindakan", "tumpuan", "tuntutan", "tuntutan", "tuntutan doj", "tuntutan sivil", "tuntutan sivil doj", "umno", "umno", "umno", "umno pemilihan", "undi", "undi", "undi", "urusan", "urusan", "urusan perniagaan", "usaha", "usaha", "usaha", "usahawan", "usahawan wanita", "wang", "wang", "wang", "wanita", "wujud", "wujud", "wujud"]}, "R": 30, "lambda.step": 0.01, "plot.opts": {"xlab": "PC1", "ylab": "PC2"}, "topic.order": [8, 10, 1, 5, 2, 7, 6, 9, 4, 3]};
    
    function LDAvis_load_lib(url, callback){
      var s = document.createElement('script');
      s.src = url;
      s.async = true;
      s.onreadystatechange = s.onload = callback;
      s.onerror = function(){console.warn("failed to load library " + url);};
      document.getElementsByTagName("head")[0].appendChild(s);
    }
    
    if(typeof(LDAvis) !== "undefined"){
       // already loaded: just create the visualization
       !function(LDAvis){
           new LDAvis("#" + "ldavis_el8739156648247841161749766", ldavis_el8739156648247841161749766_data);
       }(LDAvis);
    }else if(typeof define === "function" && define.amd){
       // require.js is available: use it to load d3/LDAvis
       require.config({paths: {d3: "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min"}});
       require(["d3"], function(d3){
          window.d3 = d3;
          LDAvis_load_lib("https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.js", function(){
            new LDAvis("#" + "ldavis_el8739156648247841161749766", ldavis_el8739156648247841161749766_data);
          });
        });
    }else{
        // require.js not available: dynamically load d3 & LDAvis
        LDAvis_load_lib("https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js", function(){
             LDAvis_load_lib("https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.js", function(){
                     new LDAvis("#" + "ldavis_el8739156648247841161749766", ldavis_el8739156648247841161749766_data);
                })
             });
    }
    </script>



Train NMF model
---------------

.. code:: ipython3

    nmf = malaya.topic_model.nmf(corpus,10)
    nmf.top_topics(5, top_n = 10, return_df = True)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>topic 0</th>
          <th>topic 1</th>
          <th>topic 2</th>
          <th>topic 3</th>
          <th>topic 4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>negara</td>
          <td>negara</td>
          <td>menteri</td>
          <td>mdb</td>
          <td>projek</td>
        </tr>
        <tr>
          <th>1</th>
          <td>bangun</td>
          <td>wang</td>
          <td>perdana</td>
          <td>niaga</td>
          <td>jual</td>
        </tr>
        <tr>
          <th>2</th>
          <td>sedia</td>
          <td>ancang</td>
          <td>perdana menteri</td>
          <td>doj</td>
          <td>syarikat</td>
        </tr>
        <tr>
          <th>3</th>
          <td>kongsi</td>
          <td>maju</td>
          <td>seri</td>
          <td>urus</td>
          <td>sewa</td>
        </tr>
        <tr>
          <th>4</th>
          <td>alam</td>
          <td>bidang</td>
          <td>najib</td>
          <td>low</td>
          <td>jual syarikat</td>
        </tr>
        <tr>
          <th>5</th>
          <td>malaysia</td>
          <td>ekonomi</td>
          <td>menteri seri</td>
          <td>jho</td>
          <td>swasta</td>
        </tr>
        <tr>
          <th>6</th>
          <td>kongsi alam</td>
          <td>industri</td>
          <td>menteri seri najib</td>
          <td>urus niaga</td>
          <td>indonesia</td>
        </tr>
        <tr>
          <th>7</th>
          <td>alam bangun</td>
          <td>latih</td>
          <td>perdana menteri seri</td>
          <td>jho low</td>
          <td>tanah</td>
        </tr>
        <tr>
          <th>8</th>
          <td>selatan</td>
          <td>dagang</td>
          <td>razak</td>
          <td>tuntut</td>
          <td>rana</td>
        </tr>
        <tr>
          <th>9</th>
          <td>kongsi alam bangun</td>
          <td>didik</td>
          <td>najib razak</td>
          <td>sivil</td>
          <td>kena</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    nmf.get_sentences(5)




.. parsed-literal::

    ['sedia kongsi alam bangun ekonomi sosial negara bangun rangka program kerjasama teknikal malaysia mtcp sedia malaysia kongsi alam bangun negara negara selatan selatan',
     'sedia kongsi alam bangun ekonomi sosial negara bangun rangka program kerjasama teknikal malaysia mtcp sedia malaysia kongsi alam bangun negara negara selatan selatan',
     'kali kongsi maklumat kena pelbagai khidmat biaya program sedia usahawan wanita iks sabah kongsi idea alam aspirasi promosi produk peringkat luas',
     'mou memorandum persefahaman arab saudi bidang selamat kongsi alam pakar malaysia deradikalisasi ganas khusus daesh',
     'terusi bentang bajet raja sedia promosi tingkat mudah lancong negara']



.. code:: ipython3

    nmf.get_topics(10)




.. parsed-literal::

    [(0,
      'negara bangun sedia kongsi alam malaysia kongsi alam alam bangun selatan kongsi alam bangun'),
     (1, 'negara wang ancang maju bidang ekonomi industri latih dagang didik'),
     (2,
      'menteri perdana perdana menteri seri najib menteri seri menteri seri najib perdana menteri seri razak najib razak'),
     (3, 'mdb niaga doj urus low jho urus niaga jho low tuntut sivil'),
     (4,
      'projek jual syarikat sewa jual syarikat swasta indonesia tanah rana kena'),
     (5,
      'rakyat malaysia negara rakyat malaysia pimpin pimpin negara maklumat kait asas pandang'),
     (6,
      'parti umno tangguh pilih lembaga putus jalan tangguh pilih pilih parti tangguh pilih parti'),
     (7, 'ajar raja tingkat laku ajar ajar proses didik bidang maju laku raja'),
     (8,
      'bangun malaysia kawasan alam bangun kawasan main bandar kongsi kongsi alam peran'),
     (9,
      'asli masyarakat jakoa bangun perdana ganti arus arus perdana pelopor bangun arus perdana')]



Train LSA model
---------------

.. code:: ipython3

    lsa = malaya.topic_model.lsa(corpus,10)
    lsa.top_topics(5, top_n = 10, return_df = True)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>topic 0</th>
          <th>topic 1</th>
          <th>topic 2</th>
          <th>topic 3</th>
          <th>topic 4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>negara</td>
          <td>negara</td>
          <td>negara</td>
          <td>mdb</td>
          <td>projek</td>
        </tr>
        <tr>
          <th>1</th>
          <td>bangun</td>
          <td>wang</td>
          <td>maju</td>
          <td>niaga</td>
          <td>jual</td>
        </tr>
        <tr>
          <th>2</th>
          <td>malaysia</td>
          <td>menteri</td>
          <td>maju bidang</td>
          <td>doj</td>
          <td>malaysia</td>
        </tr>
        <tr>
          <th>3</th>
          <td>kongsi</td>
          <td>mdb</td>
          <td>bidang</td>
          <td>urus</td>
          <td>raja</td>
        </tr>
        <tr>
          <th>4</th>
          <td>alam</td>
          <td>raja</td>
          <td>teknikal</td>
          <td>jho</td>
          <td>syarikat</td>
        </tr>
        <tr>
          <th>5</th>
          <td>kongsi alam</td>
          <td>didik</td>
          <td>didik</td>
          <td>urus niaga</td>
          <td>tingkat</td>
        </tr>
        <tr>
          <th>6</th>
          <td>sedia</td>
          <td>maju</td>
          <td>negara negara</td>
          <td>low</td>
          <td>ajar</td>
        </tr>
        <tr>
          <th>7</th>
          <td>selatan</td>
          <td>bidang</td>
          <td>tani</td>
          <td>jho low</td>
          <td>sewa</td>
        </tr>
        <tr>
          <th>8</th>
          <td>alam bangun</td>
          <td>maju bidang</td>
          <td>negara maju bidang</td>
          <td>tuntut</td>
          <td>jual syarikat</td>
        </tr>
        <tr>
          <th>9</th>
          <td>kongsi alam bangun</td>
          <td>rakyat</td>
          <td>tani didik latih</td>
          <td>tuntut sivil</td>
          <td>rakyat</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    lsa.get_sentences(5)




.. parsed-literal::

    ['sedia kongsi alam bangun ekonomi sosial negara bangun rangka program kerjasama teknikal malaysia mtcp sedia malaysia kongsi alam bangun negara negara selatan selatan',
     'sedia kongsi alam bangun ekonomi sosial negara bangun rangka program kerjasama teknikal malaysia mtcp sedia malaysia kongsi alam bangun negara negara selatan selatan',
     'negara bangun malaysia main peran kongsi alam mahir bangun kawasan bandar',
     'negara bangun malaysia main peran kongsi alam mahir bangun kawasan bandar',
     'bantu negara negara maju bidang ancang ekonomi wang dagang tani didik latih teknikal industri diplomasi']



.. code:: ipython3

    lsa.get_topics(10)




.. parsed-literal::

    [(0,
      'negara bangun malaysia kongsi alam kongsi alam sedia selatan alam bangun kongsi alam bangun'),
     (1, 'negara wang menteri mdb raja didik maju bidang maju bidang rakyat'),
     (2,
      'negara maju maju bidang bidang teknikal didik negara negara tani negara maju bidang tani didik latih'),
     (3, 'mdb niaga doj urus jho urus niaga low jho low tuntut tuntut sivil'),
     (4,
      'projek jual malaysia raja syarikat tingkat ajar sewa jual syarikat rakyat'),
     (5,
      'parti pilih rakyat tangguh umno pimpin negara malaysia rakyat malaysia tangguh pilih'),
     (6,
      'rakyat malaysia menteri bangun asli perdana kawasan negara bangun kawasan main'),
     (7,
      'ajar tingkat ajar ajar proses raja bidang didik tingkat maju raja tingkat maju laku raja tingkat didik proses'),
     (8,
      'bangun projek bandar kawasan bangun kawasan main mahir peran kongsi alam peran kongsi kawasan bandar'),
     (9,
      'asli masyarakat jakoa bangun arus perdana pelopor ganti arus arus perdana bangun arus masyarakat asli')]



