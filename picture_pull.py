import requests
import shutil


pic_dict = {}

# ultra
pic_dict['bance'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt98c1257f106d3a4b/5e1ca4dfe452e70d590e601c/Toronto_Ultra_Bance_0022_S-350x350.png'
pic_dict['brack'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltf013cb3ab88cf641/5e1ca4e0e826a50de7d6e0f7/Toronto_Ultra_Brack_0073_S-350x350.png'
pic_dict['cammy'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt7b8d4403a30e3a73/5e1ca4e02f5c0b0d43044415/Toronto_Ultra_Cammy_0139_S-350x350.png'
pic_dict['classic'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt6b8cb58e81868f2c/5e1ca4e0bed4930dd1fb8396/Toronto_Ultra_Classic_0029_S-350x350.png'
pic_dict['cleanx'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt7a0e1c0cb451293a/5e1ca4e02695ea0db4ea223d/Toronto_Ultra_CleanX_0028_S-350x350.png'
pic_dict['loony'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltd995decde78efa40/5e1ca4e06db6bb0d4e65d050/Toronto_Ultra_Loony_0061_S-350x350.png'
pic_dict['lucky'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blta1dcb8f1e9a4618f/5e1ca4e04c00fc0d64d6745c/Toronto_Ultra_Lucky_0030_S-350x350.png'
pic_dict['mayhem'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt49df1a1b7c057803/5e1ca4e047c8570ddc3ce5cc/Toronto_Ultra_Mayhem_0022_S-350x350.png'
pic_dict['methodz'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltf11ad9b831d76c2e/5e1ca4e0195bad0d9e552490/Toronto_Ultra_Methodz_0030_S-350x350.png'
pic_dict['mettalz'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt4c7d0a7650790bb5/5e1ca602f4e8170dbf330cab/Toronto_Ultra_MeTTalZ_0065_S-350x350.png'

#faze 
pic_dict['abezy'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt8161798aa0a4fba0/5e1cb2e32f5c0b0d43044599/Atlanta_Faze_Abezy_0035_S-350x350.png'
pic_dict['cellium'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt8161798aa0a4fba0/5e1cb2e32f5c0b0d43044599/Atlanta_Faze_Abezy_0035_S-350x350.png'
pic_dict['grvty'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltae3d5ea9def7ac51/5e1cb2e3bfaf010dc685ef35/Atlanta_Faze_GRVTY_0021_S-350x350.png'
pic_dict['jurnii'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['majormaniak'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt41f72b863e4b4575/5e1cb32447c8570ddc3ce756/Atlanta_Faze_MajorManiak_0030_S-350x350.png'
pic_dict['priestahh'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt22447a71d2236a1b/5e1cb2e3bed4930dd1fb8513/Atlanta_Faze_Priestahh_0021_S-350x350.png'
pic_dict['simp'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt1694036a9b06fee3/5e1cb2e3e452e70d590e6163/Atlanta_Faze_Simp_0022_S-350x350.png'

#huntsmen
pic_dict['arcitys'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt3a9eb838cbe07e16/5e1cb587e826a50de7d6e26b/Chicago_Huntsmen_Arcitys_0017_S-350x350.png'
pic_dict['envoy'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltfe87107ccc5c6d66/5e1cb587bfaf010dc685ef46/Chicago_Huntsmen_Envoy_0048_S-350x350.png'
pic_dict['formal'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltaebf3bd40a9aa167/5e1cb587230f830da963e14e/Chicago_Huntsmen_Formal_0006_S-350x350.png'
pic_dict['general'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt8cce819720a3519c/5e1cb593e452e70d590e6177/Chicago_Huntsmen_General_0029_S-350x350.png'
pic_dict['gunless'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt1e61a296881ffdd1/5e1cb593bed4930dd1fb8521/Chicago_Huntsmen_Gunless_0016_S-350x350.png'
pic_dict['mboze'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blte36eee0f2df15347/5e1cb587195bad0d9e55262b/Chicago_Huntsmen_BoZe_0021_S-350x350.png'
pic_dict['scump'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltc777275ad9bbebe9/5e1cb5936db6bb0d4e65d1c5/Chicago_Huntsmen_Scump_0029_S-350x350.png'
pic_dict['sender'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'

#empire
pic_dict['crimsix'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['huke'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt374eb71a335644ac/5e1cb5b2f4e8170dbf330e42/Dallas_Empire_Huke_0035_S-350x350.png'
pic_dict['shotzzy'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt0db78bac1611c3fb/5e1cb5b24c00fc0d64d67583/Dallas_Empire_Shotzzy_0093_S-350x350.png'
pic_dict['tommey'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltc98c3fec5c33138a/5e1cb5b26db6bb0d4e65d1cb/Dallas_Empire_Tommey_0025_S-350x350.png'
pic_dict['clayster'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt7bd5b45bc02c323f/5e1cb5b22695ea0db4ea238e/Dallas_Empire_Clayster_0137_S-350x350.png'
pic_dict['illey'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['tisch'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt0f78379cae75ada6/5e1cb5b2e452e70d590e617d/Dallas_Empire_Tisch_0042_S-350x350.png'

# mutineers
pic_dict['atura'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt03c73d94db16c110/5e1cb5d2195bad0d9e552637/Florida_Mutineers_Atura_0039_S-350x350.png'
pic_dict['frosty'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt47712fc649c7b45d/5e1cb5d22f5c0b0d430445a3/Florida_Mutineers_Frosty_0065_S-350x350.png'
pic_dict['havok'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt6684c7f0831b3fa2/5e1cb5d2bfaf010dc685ef4c/Florida_Mutineers_Havok_0021_S-350x350.png'
pic_dict['maniac'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt3aff7aff6930e7f4/5e1cb5d2230f830da963e154/Florida_Mutineers_Maniac_0081_S-350x350.png'
pic_dict['maux'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt88d9982ff9458b7a/5e1cb5d24c00fc0d64d67589/Florida_Mutineers_Maux_0038_S-350x350.png'
pic_dict['prestinni'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltfa5eacbbbe8cf415/5e1cb5d22695ea0db4ea2394/Florida_Mutineers_Prestinni_0226_S-350x350.png'
pic_dict['skyz'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltb2ab1156dac96507/5e1cb5d247c8570ddc3ce76c/Florida_Mutineers_Skyz_0032_S-350x350.png'
pic_dict['fero'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'

#ravens
pic_dict['dylan'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt8e4d8edfe3931e41/5e1cb64f6db6bb0d4e65d1dd/London_RoyalRavens_Dylan_0053_S-350x350.png'
pic_dict['jurd'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltd1bd467774bf9b2f/5e1cb64f2f5c0b0d430445b5/London_RoyalRavens_Jurd_0008_S-350x350.png'
pic_dict['madcat'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['rated'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt4b310d4e777b97ee/5e1cb64fe826a50de7d6e277/London_RoyalRavens_Rated_0116_S-350x350.png'
pic_dict['seany'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['skrapz'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt494409904fe50531/5e1cb64f230f830da963e16e/London_RoyalRavens_Skrapz_0029_S-350x350.png'
pic_dict['wuskin'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt3007d9944df3626c/5e1cb64fbfaf010dc685ef58/London_RoyalRavens_Wuskin_0045_S-350x350.png'

#guerrillas
pic_dict['aches'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['aqua'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltc7930140ea468ef2/5e1cb6176db6bb0d4e65d1d1/LA_Guerillas_AquA_0065_S-350x350.png'
pic_dict['blazt'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt027b1cb2ac58dd3a/5e1cb617230f830da963e162/LA_Guerillas_Blazt_0042_S-350x350.png'
pic_dict['lacefield'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt105ec68c382a4206/5e1cb617bfaf010dc685ef52/LA_Guerillas_Lacefield_0052_S-350x350.png'
pic_dict['ricky'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blta0acc1a33b542a07/5e1cb617e826a50de7d6e271/LA_Guerillas_Ricky_0060_S-350x350.png'
pic_dict['saints'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt264135dfba3b394c/5e1cb617bed4930dd1fb852f/LA_Guerillas_Saints_0033_S-350x350.png'
pic_dict['spart'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['vivid'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'

# rokkr
pic_dict['alexx'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt16346ec2877bd90c/5e1cb667195bad0d9e552643/Minnesota_Rokkr_Alexx_0020_S-350x350.png'
pic_dict['asim'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltf5f5bef962dbce58/5e1cb667230f830da963e174/Minnesota_Rokkr_Asim_0115_S-350x350.png'
pic_dict['assault'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltbb5dc81bf900d9b2/5e1cb6674c00fc0d64d6758f/Minnesota_Rokkr_Assault_0030_S-350x350.png'
pic_dict['exceed'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt1179c8aeb10cb0d7/5e1cb6672f5c0b0d430445bb/Minnesota_Rokkr_Exceed_0033_S-350x350.png'
pic_dict['godrx'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blta8a55bf9f3d854c9/5e1cb6672695ea0db4ea23a0/Minnesota_Rokkr_GodRX_0009_S-350x350.png'
pic_dict['silly'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt7be0313f6fda7462/5e1cb667bfaf010dc685ef5e/Minnesota_Rokkr_Silly_0095_S-350x350.png'
pic_dict['ttinyy'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt4502758bfeab95f7/5e1cb666e826a50de7d6e27d/Minnesota_Rokkr_TTinyy_0042_S-350x350.png'

#subliners
pic_dict['accuracy'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt941fe65df2b40835/5e1cb6896db6bb0d4e65d1e3/NewYork_Subliners_Accuracy_0019_S-350x350.png'
pic_dict['censor'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blta40bf668282b02b5/5e1cb6892f5c0b0d430445c1/NewYork_Subliners_Attach_0717_S-350x350.png'
pic_dict['happy'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt98896bbd7ee9e6a5/5e1cb689195bad0d9e552649/NewYork_Subliners_Happy_0045_S-350x350.png'
pic_dict['temp'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltaa152403cac34a8a/5e1cb6894c00fc0d64d67595/NewYork_Subliners_Temp_0034_S-350x350.png'
pic_dict['zero'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt945efe136ede4659/5e1cb689e826a50de7d6e283/NewYork_Subliners_Zer0_0025_S-350x350.png'
pic_dict['zoomaa'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt677f5e4eed2a06ef/5e1cb689230f830da963e17a/NewYork_Subliners_ZooMaa_0367_S-350x350.png'

#optic
pic_dict['chino'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt126684eaf9372648/5e1cb6346db6bb0d4e65d1d7/LA_Optic_Chino_0026_S-350x350.png'
pic_dict['dashy'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltc36149bd0389ac3b/5e1cb634bed4930dd1fb8535/LA_Optic_Dashy_0089_S-350x350.png'
pic_dict['goonjar'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['jkap'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt910457de927aa1b1/5e1cb634195bad0d9e55263d/LA_Optic_Jkap_0006_S-350x350.png'
pic_dict['slasher'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltbc35b8bee8724eee/5e1cb634230f830da963e168/LA_Optic_Slasher_0054_S-350x350.png'
pic_dict['kuavo'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['tjhaly'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltbacb6ca12241bde7/5e1cb634f4e8170dbf330e48/LA_Optic_TJHaly_0006_S-350x350.png'

#legion
pic_dict['breszy'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['denz'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltc43b070bfb0e7446/5e1cb6a14c00fc0d64d6759b/Paris_Legion_Denz_0060_S-350x350.png'
pic_dict['kismet'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltc6e87240521885df/5e1cb6a22695ea0db4ea23a6/Paris_Legion_KiSMET_0060_S-350x350.png'
pic_dict['louqa'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['phantomz'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt7e3141a891210537/5e1cb6a247c8570ddc3ce772/Paris_Legion_Phantomz_0041_S-350x350.png'
pic_dict['shockz'] = r'https://s3.amazonaws.com/mlg-gamebattles-production/assets/arenacp/files/1572730949/Default_Player_Headshot%20%282%29.png'
pic_dict['zed'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt10a603a92e3c520b/5e1cb6a1e826a50de7d6e289/Paris_Legion_Zed_0078_S-350x350.png'

# surge
pic_dict['apathy'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt483bc50b844db1a9/5e1cb6b747c8570ddc3ce778/Seattle_Surge_Apathy_0023_S-350x350.png'
pic_dict['enable'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt6aa86dce953c3618/5e1cb6b7f4e8170dbf330e4e/Seattle_Surge_Enable_0055_S-350x350.png'
pic_dict['karma'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt25904c589959627e/5e1cb6b76db6bb0d4e65d1e9/Seattle_Surge_Karma_0068_S-350x350.png'
pic_dict['octane'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt0c525dd17ee4cd5d/5e1cb6b74c00fc0d64d675a1/Seattle_Surge_Octane_0044_S-350x350.png'
pic_dict['pandur'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt4fc517b425b05d84/5e1cb6b7195bad0d9e55264f/Seattle_Surge_Pandur_0071_S-350x350.png'
pic_dict['proto'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt3a694976f84222da/5e1cb6b7e452e70d590e6183/Seattle_Surge_Proto_0069_S-350x350.png'
pic_dict['slacked'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt76712f9032fea27b/5e1cb6b72695ea0db4ea23ac/Seattle_Surge_Slacked_0049_S-350x350.png'


for x in pic_dict.keys():
    url = pic_dict[x]
    response = requests.get(url, stream=True)
    with open(f'assets/{x}.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    
team_dict = {}
team_dict['ATL'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt9e748f41b10f329c/5dc489f10386806c8e4e0b65/ATL-FAZ_Alternate-Logo-2.svg'
team_dict['CHI'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltb3e75a34f7b3a7c8/5dbb3a730386806c8e4e067b/CHI_-_Huntsmen.svg'
team_dict['DAL'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltf333725f060a6231/5dabbcb161bae97f636adbcc/DAL_-_Empire.svg'
team_dict['FL'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltcb76ee572edb9eb1/5db6f301afa1e66c2c3e67c8/FLA_-_Mutineers.svg'
team_dict['LON'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt5edc59dbbfc88667/5da5fabf3412200466759b94/LON_Alternate-Logo.svg'
team_dict['LAG'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltf8a143b45301c312/5dc48b33f4eb996c3143cd7b/LOS_-_Guerrillas.svg'
team_dict['MIN'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt685f76976e5310ed/5db84de2f9bc554996993be4/MIN_-_ROKKR.svg'
team_dict['NY'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt9fe05d38b5a052b6/5dadecc07561c86c84a4bb18/NYC_-_Subliners.svg'
team_dict['OGLA'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltdaaf0729dc8b4bc8/5db1d99aa5d2cf498cbba159/LAS_-_OpTic_Gaming.svg'
team_dict['PAR'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/blt7c039a2766790e32/5dbdac971af57b7f5dfa2df1/PAR_-_Legion.svg'
team_dict['SEA'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltbe8507a1cef478bb/5dba15def9bc554996993cd0/SEA_-_Surge.svg'
team_dict['TOR'] = r'https://images.blz-contentstack.com/v3/assets/blta7b34f1f894a2422/bltcdbf12f8e1f145b1/5dc447c37561c86c84a4c3dd/Group_4.svg'

for x in team_dict.keys():
    url = team_dict[x]
    response = requests.get(url, stream=True)
    with open(f'assets/{x}.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response