from calculator import Workload
from calculator import Resource
from calculator import Engine
from pprint import pprint
import yaml
from time import sleep


def get_workload(mean, var):

    # Create a workload with a specific number of tasks with number of
    # operations per task drawn from a distribution
    wl = Workload(  num_tasks=128,          # no. of tasks
                    ops_dist='normal',     # distribution to draw samples from
                    dist_mean=mean,         # mean of distribution
                    dist_var=var             # variance of distribution
                )

    return wl


def get_resource(mean, t_var, s_var):

    # Create a resource with a specific number of cores with performance of each
    # core drawn from a distribution
    res = Resource( num_cores=128,        # no.
                    perf_dist='normal',# distribution to draw samples from
                    dist_mean=mean,        # mean of distribution
                    temporal_var=t_var,     # temporal variance of core performance
                    spatial_var=s_var     # spatial variance of core performance
                )

    return res


def get_engine(res):

    eng = Engine(cfg_path='./config.yml')
    eng.assign_cfg()
    eng.assign_resource(res)
    return eng


if __name__ == '__main__':

    
    # Create WLMS instance with a workload, resource, selection criteria, and
    # binding criteria
    for var in [0,2,4,8]:

        t = 0
        res = get_resource(mean=32, t_var=var, s_var=0)
        eng = get_engine(res)
        for _ in range(8):

            wl = get_workload(mean=1024, var=0)
            eng.assign_workload(wl, submit_at=t)
            t += 5
        
        sleep(5)