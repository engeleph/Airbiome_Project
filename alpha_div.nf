nextflow.enable.dsl=2

workflow {
  next = params.basedir + "/output_test/group_" + params.group + "/metaphlan3/db4/" + params.sampleName + "_db4.metaphlan3.biom"
  next = qza_table(next)
  next = alpha_diversity(next)
}

process qza_table {
	publishDir "${params.basedir}/output_test/group_${params.group}/alpha_diversity", mode: 'copy', pattern: "*.{qza}"

        input:
	path("${params.sampleName}_db4.metaphlan3.biom")

        output:                            
        file "${params.sample}_abundance_table.qza"

	script:
        """
        #It checks if the profiling was successful, that is if identifies at least three species
        qiime tools import --input-path ${params.sampleName}_db4.metaphlan3.biom --type 'FeatureTable[Frequency]' --input-format BIOMV100Format --output-path ${params.sample}_abundance_table.qza

        """

}
process alpha_diversity {

        publishDir "${params.basedir}/output_test/group_${params.group}/alpha_diversity", mode: 'copy', pattern: "*.{tsv}"
       
        input:
        file("${params.sample}_abundance_table.qza")
 

        output: 
	file "${params.sample}_alpha_diversity.tsv"


        script:
        """
        #It checks if the profiling was successful, that is if identifies at least three species
        echo "${params.sample}" > ${params.sample}_alpha_diversity.tsv
        for alpha in ace berger_parker_d brillouin_d chao1 dominance enspie esty_ci fisher_alpha gini_index goods_coverage heip_e kempton_taylor_q lladser_pe margalef mcintosh_d mcintosh_e menhinick michaelis_menten_fit pielou_e robbins shannon simpson simpson_e strong
        do
            qiime diversity alpha --i-table ${params.sample}_abundance_table.qza --p-metric \$alpha --output-dir \$alpha 
            qiime tools export --input-path \$alpha/alpha_diversity.qza --output-path \${alpha} 
            value=\$(sed -n '2p' \${alpha}/alpha-diversity.tsv | cut -f 2)
 
            echo -e  \$alpha'\t'\$value 
        done  >> ${params.sample}_alpha_diversity.tsv
	sed -i '/Saved/d' ${params.sample}_alpha_diversity.tsv
        sed -i '/Exported/d' ${params.sample}_alpha_diversity.tsv

        """
}






