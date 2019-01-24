# myeloma
clinical trial IR and Topic Models

When a patient is forced down the track of clinical trials, their ability to make informed medical and life decisions can be greatly limited by the vast amount of information in both structured and unstructured text. Inability to efficiently skim through this information also limits their communication bandwidth with medical professionals.

In the case of myeloma, several trial immunotherapy strategies exist. Traditional treatments of multiple myeloma focus on persistent reduction in plasma cells with maintenance therapy. More recently, strategies are broken down to specific modifications or implementations CAR-T, BiTEs, and Immuno Checkpoint Inhibitors, for example. Specific cases of CAR-T (chimeric antigen receptor) treatments include strategies targeting BCMA, CD138, and CD19 ( and others ) antigens.

Chimeric antigen receptor T-cell (CAR-T) strategies genetically modify T-Cells to include a linker designed to bind with a specific antigen expressed on the target diseased cell. The modified T-Cell recognizes or has specificity to the antigen on the diseased cell, and, once bound, is activated thereby killing the cancer.

For my project, I would like to work towards a semi supervised non-parametric topic modeling system in order to Cluster classes of treatment strategies. This model would likely need to be informed by a named entity recognizer, and possibly some taxonomic constraints, which would be the semi supervising material. I don't yet know how the clustering model would be best informed.

I would like to be able to answer two questions.

How many different treatments strategies are used in myeloma clinical trials?
What are the clinical site locations for each of these treatments?
I have found a named entity recognizer called Cliner, and have several ideas for topic modeling from frequent itemset pairings to extensions of the latent dirichlet allocation model.
