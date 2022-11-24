from tokenize import Double
import numpy as np
from scipy.stats import gaussian_kde
import multiprocessing as mp
class ConfidenceEstimator:
    
    def __init__(self, fr_model_name, db_name):

        self._db_name = db_name
        self._fr_model_name = fr_model_name
        # load scores
        path = "../../Data//" + fr_model_name + "//" 
        self._scores_gen = np.load(path + "scores_gen_"+ db_name + ".npy")
        self._scores_imp = np.load(path + "scores_imp_"+ db_name + ".npy")

        self._kde_gen = gaussian_kde(self._scores_gen)
        self._kde_imp = gaussian_kde(self._scores_imp)
        
    def confidence(self, score_list, dist_name,to_fuse=0):
        """ Returns the probability that the scores belong to 
            a certain distribution.
            
            score_list: list, list of comparison scores
            dist_name: str, either "gen" or "imp"
            to_fuse: int, number of scores to fuse
        """
        # compute kde probabilities
        probs_gen = np.zeros((score_list.shape[0],to_fuse))
        probs_imp = np.zeros((score_list.shape[0],to_fuse))
        
        # compute confidence scores for each column
        for column in range(new_score_list.shape[1]):
            probs_gen[:,column] = parrallel_score_samples(self._kde_gen,score_list[:,column])
            probs_imp[:,column] = parrallel_score_samples(self._kde_imp,score_list[:,column])

        # compute likelihoods
        L_gen = np.prod(probs_gen,axis=1)
        L_imp = np.prod(probs_imp,axis=1)
        
        if dist_name == "gen":
            return L_gen / (L_gen + L_imp)
        
        elif dist_name == "imp":
            return L_imp / (L_gen + L_imp)
        
        
    def confidence_single(self, score_list, dist_name):
        """ Returns the probability for EACH SCORE SEPARATELY that it belongs  
            to a certain distribution.
            
            score_list: list/arr, list of comparison scores
            dist_name: str, either "gen" or "imp"
        """
        # compute kde probabilities
        L_gen = parrallel_score_samples(self._kde_gen,score_list)
        L_imp = parrallel_score_samples(self._kde_imp,score_list)
        
        
        if dist_name == "gen":
            return L_gen / (L_gen + L_imp)
        
        elif dist_name == "imp":
            return L_imp / (L_gen + L_imp)
       

mp.set_start_method('fork')
def parrallel_score_samples(kde, samples, thread_count=int(.8 * mp.cpu_count())):
    with mp.Pool(processes=thread_count) as p:
        return np.concatenate(p.map(kde.pdf, np.array_split(samples, thread_count)))


        
