import numpy as np

from collections import OrderedDict

big_range = np.array([200,1000,6000,20000])
small_range = np.array([200,1000,6000])

products = OrderedDict([
    ('Ar', {
      'coeffs':[
            [ 0.000000000e+00, 0.000000000e+00, 2.500000000e+00, 0.000000000e+00, 0.000000000e+00, # 200 - 1000
              0.000000000e+00, 0.000000000e+00, -7.453750000e+02, 4.379674910e+00],
            [ 2.010538475e+01, -5.992661070e-02, 2.500069401e+00, -3.992141160e-08, 1.205272140e-11, # 1000 - 6000
              -1.819015576e-15, 1.078576636e-19, -7.449939610e+02, 4.379180110e+00],
            [ -9.951265080e+08, 6.458887260e+05, -1.675894697e+02, 2.319933363e-02, -1.721080911e-06, # 6000 - 20000
              6.531938460e-11, -9.740147729e-16, -5.078300340e+06,  1.465298484e+03]
      ],
      'ranges': big_range,
      'wt': 39.948,
      'elements': {'Ar': 1}
    }),
    # 'C': {
    #   'coeffs': [
    #         [6.495031470e+02, -9.649010860e-01, 2.504675479e+00, -1.281448025e-05, 1.980133654e-08, # 200 - 1000
    #          -1.606144025e-11, 5.314483411e-15, 8.545763110e+04, 4.747924288e+00,],
    #         [-1.289136472e+05, 1.719528572e+02, 2.646044387e+00, -3.353068950e-04, 1.742092740e-07, # 1000 - 6000
    #          -2.902817829e-11, 1.642182385e-15, 8.410597850e+04, 4.130047418e+00],
    #         [4.432528010e+08, -2.886018412e+05, 7.737108320e+01, -9.715281890e-03, 6.649595330e-07, # 6000 - 20000
    #          -2.230078776e-11, 2.899388702e-16, 2.355273444e+06, -6.405123160e+02,]
    #   ],
    #   'ranges': big_range,
    #   'wt': 12.0170,
    #   'elements': {'C': 1}
    # },
    ('CO', {
      'coeffs':[
            [ 1.489045326e+04, -2.922285939e+02, 5.724527170e+00, -8.176235030e-03, # 200 - 1000
              1.456903469e-05, -1.087746302e-08, 3.027941827e-12, -1.303131878e+04, -7.859241350e+00],
            [ 4.619197250e+05, -1.944704863e+03, 5.916714180e+00, -5.664282830e-04, # 1000 - 6000
              1.398814540e-07, -1.787680361e-11, 9.620935570e-16, -2.466261084e+03, -1.387413108e+01],
            [ 8.868662960e+08, -7.500377840e+05, 2.495474979e+02, -3.956351100e-02, # 6000 - 20000
              3.297772080e-06, -1.318409933e-10, 1.998937948e-15,  5.701421130e+06, -2.060704786e+03],
      ],
      'ranges': big_range,
      'wt': 28.0101,
      'elements': OrderedDict([('C', 1), ('O', 1)])
    }),
    ('CO2', {
      'coeffs':[
            [ 4.943650540e+04, -6.264116010e+02,  5.301725240e+00,  2.503813816e-03, # 200 - 1000
              -2.127308728e-07, -7.689988780e-10,  2.849677801e-13, -4.528198460e+04, -7.048279440e+00, ],
            [ 1.176962419e+05, -1.788791477e+03,8.291523190e+00,-9.223156780e-05, # 1000 - 6000
              4.863676880e-09, -1.891053312e-12,6.330036590e-16,-3.908350590e+04, -2.652669281e+01],
            [ -1.544423287e+09, 1.016847056e+06, -2.561405230e+02,  3.369401080e-02, # 6000 - 20000
              -2.181184337e-06, 6.991420840e-11, -8.842351500e-16, -8.043214510e+06,  2.254177493e+03]
      ],
      'ranges': big_range,
      'wt': 44.0095,
      'elements': OrderedDict([('C', 1), ('O', 2)])
    }),
    ('H', {
      'coeffs':[
           [ 0.000000000e+00, 0.000000000e+00, 2.500000000e+00, 0.000000000e+00, 0.000000000e+00,
             0.000000000e+00, 0.000000000e+00, 2.547370801e+04, -4.466828530e-01], # 200 - 1000
           [ 6.078774250e+01, -1.819354417e-01, 2.500211817e+00, -1.226512864e-07, 3.732876330e-11,
             -5.687744560e-15, 3.410210197e-19, 2.547486398e+04, -4.481917770e-01], # 1000 - 6000
           [ 2.173757694e+08, -1.312035403e+05, 3.399174200e+01, -3.813999680e-03, 2.432854837e-07,
             -7.694275540e-12, 9.644105630e-17, 1.067638086e+06, -2.742301051e+02] # 6000 - 20000
      ],
      'ranges': big_range,
      'wt': 1.00794,
      'elements': {'H':1}
    }),
    ('HO2', {
      'coeffs':[
            [ -7.598882540e+04, 1.329383918e+03, -4.677388240e+00, 2.508308202e-02, -3.006551588e-05, # 200 - 1000
              1.895600056e-08, -4.828567390e-12, -5.809366430e+03, 5.193602140e+01],
            [ -1.810669724e+06, 4.963192030e+03, -1.039498992e+00, 4.560148530e-03, -1.061859447e-06, # 1000 - 6000
              1.144567878e-10, -4.763064160e-15, -3.194418740e+04, 4.066850920e+01],
      ],
      'ranges': small_range,
      'wt': 33.00674,
      'elements': OrderedDict([('H',1), ('O',2)])
    }),
    ('H2', {
      'coeffs':[
            [ 4.078322810e+04, -8.009185450e+02, 8.214701670e+00, -1.269714360e-02,  1.753604930e-05, # 200 - 1000
              -1.202860160e-08, 3.368093160e-12, 2.682484380e+03, -3.043788660e+01],
            [ 5.608123380e+05, -8.371491340e+02, 2.975363040e+00, 1.252249930e-03, -3.740718420e-07, # 1000 - 6000
              5.936628250e-11, -3.606995730e-15, 5.339815850e+03, -2.202764050e+00],
            [ 4.966716130e+08, -3.147448120e+05, 7.983887500e+01, -8.414504190e-03,  4.753060440e-07, # 6000 - 20000
              -1.371809730e-11, 1.605374600e-16, 2.488354660e+06, -6.695524190e+02]
      ],
      'ranges': big_range,
      'wt': 2.01588,
      'elements': {'H': 2}
    }),
    ('H2O', {
      'coeffs':[
            [ -3.947960830e+04,  5.755731020e+02,  9.317826530e-01,  7.222712860e-03, -7.342557370e-06,  # 200 - 1000
              4.955043490e-09, -1.336933246e-12, -3.303974310e+04, 1.724205775e+01],
            [ 1.034972096e+06, -2.412698562e+03, 4.646110780e+00,  2.291998307e-03, -6.836830480e-07, # 1000 - 6000
              9.426468930e-11, -4.822380530e-15, -1.384286509e+04, -7.978148510e+00],
      ],
      'ranges': small_range,
      'wt': 18.01528,
      'elements': OrderedDict([('H',2), ('O',1)])
    }),
    ('H2O2', {
      'coeffs':[
            [ -9.279533580e+04,  1.564748385e+03, -5.976460140e+00,  3.270744520e-02, -3.932193260e-05, # 200 - 1000
              2.509255235e-08, -6.465045290e-12,  -2.494004728e+04,  5.877174180e+01],
            [ 1.489428027e+06, -5.170821780e+03,  1.128204970e+01, -8.042397790e-05, -1.818383769e-08, # 1000 - 6000
              6.947265590e-12, -4.827831900e-16,  1.418251038e+04, -4.650855660e+01],
      ],
      'ranges': small_range,
      'wt': 34.01468,
      'elements': OrderedDict([('H',2), ('O',2)])
    }),
    ('N', {
      'coeffs':[
            [ 0.000000000e+00, 0.000000000e+00, 2.500000000e+00, 0.000000000e+00, 0.000000000e+00,
              0.000000000e+00, 0.000000000e+00, 5.610463780e+04, 4.193909320e+00],
            [ 8.876501380e+04, -1.071231500e+02, 2.362188287e+00, 2.916720081e-04, -1.729515100e-07, # 1000 - 6000
              4.012657880e-11, -2.677227571e-15, 5.697351330e+04, 4.865235790e+00],
            [ 5.475181050e+08, -3.107574980e+05, 6.916782740e+01, -6.847988130e-03,  3.827572400e-07,  # 6000 - 20000
              -1.098367709e-11, 1.277986024e-16, 2.550585618e+06, -5.848769710e+02]
      ],
      'ranges': big_range,
      'wt': 14.00674,
      'elements': {'N':1}
    }),
    ('NH3', {
      'coeffs': [
            [ -7.681226150e+04, 1.270951578e+03, -3.893229130e+00, 2.145988418e-02, -2.183766703e-05,  # 200 - 1000
              1.317385706e-08, -3.332322060e-12, -1.264886413e+04, 4.366014940e+01],
            [ 2.452389535e+06, -8.040894240e+03, 1.271346201e+01, -3.980186580e-04,  3.552502750e-08, # 1000 - 6000
              2.530923570e-12, -3.322700530e-16, 4.386191960e+04, -6.462330250e+01]
      ],
      'ranges': small_range,
      'wt': 17.03056,
      'elements': OrderedDict([('N', 1), ('H', 3)])
    }),
    ('NO', {
      'coeffs': [
            [ -1.143916503e+04, 1.536467592e+02, 3.431468730e+00,-2.668592368e-03, 8.481399120e-06, # 200 - 1000
              -7.685111050e-09, 2.386797655e-12, 9.098214410e+03, 6.728727490e+00],
            [ 2.239018716e+05, -1.289651623e+03, 5.433936030e+00, -3.656034900e-04,  9.880966450e-08, # 1000 - 6000
              -1.416076856e-11,  9.380184620e-16, 1.750317656e+04, -8.501667090e+00],
            [ -9.575303540e+08, 5.912434480e+05, -1.384566826e+02, 1.694339403e-02, -1.007351096e-06, # 6000 - 20000
              2.912584076e-11, -3.295109350e-16, -4.677501240e+06, 1.242081218e+03]
      ],
      'ranges': big_range,
      'wt': 30.00614,
      'elements': OrderedDict([('N',1), ('O',1)])
    }),
    ('NO2', {
      'coeffs': [
           [ -5.642038780e+04, 9.633085720e+02, -2.434510974e+00, 1.927760886e-02, -1.874559328e-05,
             9.145497730e-09, -1.777647635e-12, -1.547925037e+03, 4.067851340e+01],
           [ 7.213001570e+05, -3.832615200e+03, 1.113963285e+01, -2.238062246e-03,  6.547723430e-07, # 1000 - 6000
             -7.611335900e-11,  3.328361050e-15, 2.502497403e+04, -4.305129910e+01]
      ],
      'ranges': small_range,
      'wt': 46.00554,
      'elements': OrderedDict([('N',1), ('O',2)])
    }),
    ('NO3', {
      'coeffs': [
          [ 3.405398410e+04, 2.266670652e+02, -3.793081630e+00, 4.170732700e-02, -5.709913270e-05,
            3.834158110e-08, -1.021969284e-11, 7.088112200e+03, 4.273091810e+01],
          [ -3.943872710e+05, -8.244263530e+02, 1.061325843e+01, -2.448749816e-04,  5.406060320e-08,
            -6.195466750e-12,  2.870000149e-16, 8.982011730e+03, -3.444666500e+01]
      ],
      'ranges': small_range,
      'wt': 62.00494,
      'elements': OrderedDict([('N',1), ('O',3)])
    }),
    ('N2', {
      'coeffs': [
          [ 2.210371497e+04, -3.818461820e+02, 6.082738360e+00, -8.530914410e-03,  1.384646189e-05,
            -9.625793620e-09, 2.519705809e-12, 7.108460860e+02, -1.076003316e+01],
          [ 5.877124060e+05, -2.239249073e+03,  6.066949220e+00, -6.139685500e-04,  1.491806679e-07,
            -1.923105485e-11,  1.061954386e-15, 1.283210415e+04, -1.586639599e+01],
          [ 8.310139160e+08, -6.420733540e+05, 2.020264635e+02, -3.065092046e-02,  2.486903333e-06, # 6000 - 20000
            -9.705954110e-11, 1.437538881e-15, 4.938707040e+06, -1.672099736e+03, ]
      ],
      'ranges': big_range,
      'wt': 28.01348,
      'elements': {'N': 2}
    }),
    # ('N2O',{
    #   'coeffs': [
    #     [4.288225970e+04, -6.440118440e+02,  6.034351430e+00,  2.265394436e-04,  3.472782850e-06, 
    #      -3.627748640e-09, 1.137969552e-12,  1.179405506e+04, -1.003128297e+01, ],
    #     [3.438448040e+05, -2.404557558e+03,  9.125636220e+00, -5.401667930e-04,  1.315124031e-07, 
    #      -1.414215100e-11, 6.381066870e-16,  2.198632638e+04, -3.147804743e+01, ]
    #   ],
    #   'ranges': small_range, 
    #   'wt': 44.01288,
    #   'elements': {'N':2, 'O':2}
    # }), 
    ('O', {
      'coeffs': [
          [ -7.953611300e+03, 1.607177787e+02,  1.966226438e+00,  1.013670310e-03, -1.110415423e-06, # 200 - 1000
            6.517507500e-10, -1.584779251e-13,  2.840362437e+04,  8.404241820e+00],
          [ 2.619020262e+05, -7.298722030e+02,  3.317177270e+00, -4.281334360e-04,  1.036104594e-07, # 1000 - 6000
            -9.438304330e-12, 2.725038297e-16, 3.392428060e+04, -6.679585350e-01],
          [ 1.779004264e+08, -1.082328257e+05,  2.810778365e+01, -2.975232262e-03,  1.854997534e-07, # 6000 - 20000
            -5.796231540e-12, 7.191720164e-17, 8.890942630e+05, -2.181728151e+02]
      ],
      'ranges': big_range,
      'wt': 15.99940,
      'elements': {'O': 1}
    }),
    ('OH', {
      'coeffs': [
          [ -1.998858990e+03, 9.300136160e+01, 3.050854229e+00, 1.529529288e-03, -3.157890998e-06, # 200 - 1000
            3.315446180e-09, -1.138762683e-12, 3.239683480e+03, 4.674110790e+00],
          [ 1.017393379e+06, -2.509957276e+03, 5.116547860e+00, 1.305299930e-04, -8.284322260e-08, # 1000 - 6000
            2.006475941e-11, -1.556993656e-15, 2.044487130e+04, -1.101282337e+01],
          [ 2.847234193e+08, -1.859532612e+05, 5.008240900e+01, -5.142374980e-03,  2.875536589e-07, # 6000 - 20000
            -8.228817960e-12, 9.567229020e-17, 1.468642377e+06, -4.023555580e+02]
      ],
      'ranges': big_range,
      'wt': 17.00734,
      'elements': OrderedDict([('O', 1), ('H', 1)])
    }),
    ('O2', {
      'coeffs':[
            [ -3.425563420e+04, 4.847000970e+02, 1.119010961e+00, 4.293889240e-03, # 200 - 1000
              -6.836300520e-07, -2.023372700e-09, 1.039040018e-12, -3.391454870e+03, 1.849699470e+01],
            [ -1.037939022e+06,2.344830282e+03,1.819732036e+00,1.267847582e-03, # 1000 - 6000
              -2.188067988e-07,2.053719572e-11,-8.193467050e-16,-1.689010929e+04, 1.738716506e+01],
            [ 4.975294300e+08, -2.866106874e+05,  6.690352250e+01, -6.169959020e-03,  # 6000 - 20000
              3.016396027e-07, -7.421416600e-12,  7.278175770e-17, 2.293554027e+06, -5.530621610e+02]
      ],
      'ranges': big_range,
      'wt': 31.99880,
      'elements': {'O': 2}
    })
])

element_wts = {
  'C':12.0170, 'O': 15.99940, 'Ar': 39.948, 'H': 1.00794, 'N':14.00674
}

reactants = { # used to compute the correct amounts of each product for an initial condition
  'air': OrderedDict([('N2', 78.084), ('O2', 20.9476), ('Ar', .9365), ('CO2', .0319), ('H2O', 1)]), #percentage by volume. Note the actual amount of H2O is irrelevant and will be set by WAR
  # 'air': {'N': 1.5616, 'O':.41959, 'Ar': .00936, 'C': .00032},
  'H2': OrderedDict([('H2', 1.00)]), 
}



init_prod_amounts = reactants['air'].copy() # initial value used to set the atomic fractions in the mixture
default_elements = ['Ar', 'C', 'H', 'N', 'O']


# tot_amount = 0
# for r in products.keys(): # assume pure air by default
#     r_amount = reactants['air'].get(r,0) * products[r]['wt'] # initial amounts need to be given in mass ratios
#     tot_amount += r_amount
#     init_prod_amounts[r] = r_amount


# for r in products.keys():
#     if r == "O2" or r == "N2":
#       init_prod_amounts[r] = 1
#     else:
#       init_prod_amounts[r] = 0