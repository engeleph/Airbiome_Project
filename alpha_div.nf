metaphlan_bug_list='/home/philipp/Documents/Airbiome_Project/taxprofiler/Airbiome_Project/output_test/metaphlan3/db4/1_se_SRR12170646_db4.metaphlan3.biom'
nextflow.enable.dsl=2

workflow {
  next = '/home/philipp/Documents/Airbiome_Project/taxprofiler/Airbiome_Project/output_test/metaphlan3/db4/1_se_SRR12170646_db4.metaphlan3.biom'
  next = alpha_diversity(next)
  next = remove_unnecessary_lines(next)
}

process alpha_diversity {

        publishDir "/home/philipp/Documents/Airbiome_Project/taxprofiler/Airbiome_Project/", mode: 'copy', pattern: "*.{tsv}"
        
        input:
        path(metaphlan_bug_list)

        output:
        file "sample1_alpha_diversity.tsv"


        script:
        """
        #It checks if the profiling was successful, that is if identifies at least three species
        echo "sample1" > sample1_alpha_diversity.tsv
        qiime tools import --input-path $metaphlan_bug_list --type 'FeatureTable[Frequency]' --input-format BIOMV100Format --output-path sample1_abundance_table.qza
        for alpha in ace berger_parker_d brillouin_d chao1 dominance doubles enspie esty_ci fisher_alpha gini_index goods_coverage heip_e kempton_taylor_q lladser_pe margalef mcintosh_d mcintosh_e menhinick michaelis_menten_fit pielou_e robbins shannon simpson simpson_e singles strong
        do
            qiime diversity alpha --i-table sample1_abundance_table.qza --p-metric \$alpha --output-dir \$alpha 
            qiime tools export --input-path \$alpha/alpha_diversity.qza --output-path \${alpha} 
            value=\$(sed -n '2p' \${alpha}/alpha-diversity.tsv | cut -f 2)
 
            echo -e  \$alpha'\t'\$value 
        done  >> sample1_alpha_diversity.tsv

        """
}


process remove_unnecessary_lines {
	publishDir "/home/philipp/Documents/Airbiome_Project/taxprofiler/Airbiome_Project/", mode: 'copy', pattern: "*.{tsv}"

        input:
        path "sample1_alpha_diversity.tsv"

	output:
	file "sample1_alpha_diversity.tsv"

        script:
        """
        sed -i '/Saved/d' sample1_alpha_diversity.tsv
        sed -i '/Exported/d' sample1_alpha_diversity.tsv

        """
}








