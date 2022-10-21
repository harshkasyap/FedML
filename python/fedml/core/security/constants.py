DEFENSE_NORM_DIFF_CLIPPING = "norm_diff_clipping"
DEFENSE_ROBUST_LEARNING_RATE = "robust_learning_rate"
DEFENSE_KRUM = "krum"
DEFENSE_SLSGD = "slsgd"
DEFENSE_GEO_MEDIAN = "geometric_median"
DEFENSE_CCLIP = "cclip"
DEFENSE_WEAK_DP = "weak_dp"
DEFENSE_DP = "dp"
DEFENSE_RFA = "rfa"
DEFENSE_FOOLSGOLD = "foolsgold"
DEFENSE_CRFL = "crfl"
DEFENSE_THREESIGMA = "3sigma"
DEFENSE_THREESIGMA_KRUM = "3sigma_krum"
DEFENSE_THREESIGMA_GEOMEDIAN = "3sigma_geo"
DEFENSE_MULTIKRUM = "multikrum"
DEFENSE_TRIMMED_MEAN = "trimmed_mean"

ATTACK_METHOD_BYZANTINE_ATTACK = "byzantine"
ATTACK_METHOD_DLG = "dlg"
ATTACK_LABEL_FLIPPING = "label_flipping"


"""
Dataset Constants
"""
cifar10_mean = [0.4914672374725342, 0.4822617471218109, 0.4467701315879822]
cifar10_std = [0.24703224003314972, 0.24348513782024384, 0.26158785820007324]
cifar100_mean = [0.5071598291397095, 0.4866936206817627, 0.44120192527770996]
cifar100_std = [0.2673342823982239, 0.2564384639263153, 0.2761504650115967]
mnist_mean = (0.13066373765468597,)
mnist_std = (0.30810782313346863,)
imagenet_mean = [0.485, 0.456, 0.406]
imagenet_std = [0.229, 0.224, 0.225]