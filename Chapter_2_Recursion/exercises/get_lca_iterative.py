import tax_dict as td

# uses list from tax_dict.py (global variable) 
tax_dict = td.tax_dict_1

def get_ancestors_rec(taxon):
	if taxon == 'Primates':
		return [taxon]
	else:
		parent = tax_dict.get(taxon)
		parent_ancestors = get_ancestors_rec(parent) 
		return [parent] + parent_ancestors

def get_lca(taxon1, taxon2): 
    taxon1_ancestors = [taxon1] + get_ancestors_rec(taxon1) 
    for taxon in [taxon2] + get_ancestors_rec(taxon2): 
        if taxon in taxon1_ancestors: 
            return taxon 

def get_lca_list(taxa): 
    taxon1 = taxa.pop() 
    while len(taxa) > 0: 
        taxon2 = taxa.pop() 
        lca = get_lca(taxon1, taxon2) 
        print('LCA of ' + taxon1 + ' and ' + taxon2 + ' is ' + lca) 
        taxon1 = lca 
    return taxon1 

print(get_lca_list(['Pan troglodytes','Tarsius tarsier', 'Pongo abelii']))
