for i in range(len(vpbf_pens)):

   if ien_servidores['PENSINISTA'][i] == 'Sim': # cod vitalicio

      if ien_servidores['CO_SEXO_SERVIDOR'][i] == 1:

         ax_fem_validos_tfinal = axs.loc[(axs['IDADE'] == (ien_servidores['IDADE'][i]+ien_servidores['TEMPO_FALTA_CONTRIBUICAO'][i])),['AX_FEM_VALIDOS']]['AX_FEM_VALIDOS'].iloc[0]
         lx_fem_validos_tfinal = lxs.loc[(lxs['IDADE'] == (ien_servidores['IDADE'][i]+ien_servidores['TEMPO_FALTA_CONTRIBUICAO'][i])),['LX_FEM_VALIDOS']]['LX_FEM_VALIDOS'].iloc[0]
         lx_fem_validos_idade = lxs.loc[(axs['IDADE'] == (ien_servidores['IDADE'][i])),['LX_FEM_VALIDOS']]['LX_FEM_VALIDOS'].iloc[0]
         ien_servidores['VALOR_BENF_FUT'][i] = (p * ien_servidores['BENF_PROJETADO'][i] * (v ** ien_servidores['TEMPO_FALTA_CONTRIBUICAO'][i]) * (lx_fem_validos_tfinal/lx_fem_validos_idade) *  ax_fem_validos_tfinal)
         ien_servidores['LX_IDADE'][i] = lx_fem_validos_idade
         ien_servidores['LX_TEMPOFINAL'][i] = lx_fem_validos_tfinal
         ien_servidores['ANUIDADE_TEMPOFINAL'][i] =  ax_fem_validos_tfinal

      elif ien_servidores['CO_SEXO_SERVIDOR'][i] == 2:

         ax_masc_validos_tfinal = axs.loc[(axs['IDADE'] == (ien_servidores['IDADE'][i]+ien_servidores['TEMPO_FALTA_CONTRIBUICAO'][i])),['AX_MASC_VALIDOS']]['AX_MASC_VALIDOS'].iloc[0]
         lx_masc_validos_tfinal = lxs.loc[(lxs['IDADE'] == (ien_servidores['IDADE'][i]+ien_servidores['TEMPO_FALTA_CONTRIBUICAO'][i])),['LX_MASC_VALIDOS']]['LX_MASC_VALIDOS'].iloc[0]
         lx_masc_validos_idade = lxs.loc[(axs['IDADE'] == (ien_servidores['IDADE'][i])),['LX_MASC_VALIDOS']]['LX_MASC_VALIDOS'].iloc[0]
         ien_servidores['VALOR_BENF_FUT'][i] = (p * ien_servidores['BENF_PROJETADO'][i] * (v ** ien_servidores['TEMPO_FALTA_CONTRIBUICAO'][i]) * (lx_masc_validos_tfinal/lx_masc_validos_idade) *  ax_masc_validos_tfinal)
         ien_servidores['LX_IDADE'][i] = lx_masc_validos_idade
         ien_servidores['LX_TEMPOFINAL'][i] = lx_masc_validos_tfinal
         ien_servidores['ANUIDADE_TEMPOFINAL'][i] =  ax_masc_validos_tfinal

   elif ien_servidores['CO_DURACAO'][i] == 2: # cod pensionista

      if ien_servidores['CO_SEXO_SERVIDOR'][i] == 1:

         ax_fem_validos_tfinal = axs.loc[(axs['IDADE'] == (ien_servidores['IDADE'][i]+ien_servidores['TEMPO_FINAL_APOSENTADORIA'][i])),['AX_FEM_VALIDOS']]['AX_FEM_VALIDOS'].iloc[0]
         lx_fem_validos_tfinal = lxs.loc[(lxs['IDADE'] == (ien_servidores['IDADE'][i]+ien_servidores['TEMPO_FINAL_APOSENTADORIA'][i])),['LX_FEM_VALIDOS']]['LX_FEM_VALIDOS'].iloc[0]
         lx_fem_validos_idade = lxs.loc[(axs['IDADE'] == (ien_servidores['IDADE'][i])),['LX_FEM_VALIDOS']]['LX_FEM_VALIDOS'].iloc[0]
         ien_servidores['VALOR_BENF_FUT'][i] = (p * ien_servidores['BENF_PROJETADO'][i] * (v ** ien_servidores['TEMPO_FINAL_APOSENTADORIA'][i]) * (lx_fem_validos_tfinal/lx_fem_validos_idade) *  ax_fem_validos_tfinal)

      elif ien_servidores['CO_SEXO_SERVIDOR'][i] == 2:

         ax_masc_validos_tfinal = axs.loc[(axs['IDADE'] == (ien_servidores['IDADE'][i]+ien_servidores['TEMPO_FINAL_APOSENTADORIA'][i])),['AX_MASC_VALIDOS']]['AX_MASC_VALIDOS'].iloc[0]
         lx_masc_validos_tfinal = lxs.loc[(lxs['IDADE'] == (ien_servidores['IDADE'][i]+ien_servidores['TEMPO_FINAL_APOSENTADORIA'][i])),['LX_MASC_VALIDOS']]['LX_MASC_VALIDOS'].iloc[0]
         lx_masc_validos_idade = lxs.loc[(axs['IDADE'] == (ien_servidores['IDADE'][i])),['LX_MASC_VALIDOS']]['LX_MASC_VALIDOS'].iloc[0]
         ien_servidores['VALOR_BENF_FUT'][i] = (p * ien_servidores['BENF_PROJETADO'][i] * (v ** ien_servidores['TEMPO_FINAL_APOSENTADORIA'][i]) * (lx_masc_validos_tfinal/lx_masc_validos_idade) *  ax_masc_validos_tfinal)