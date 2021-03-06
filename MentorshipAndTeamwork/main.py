import copy
import sys
import random as rnd
from typing import List

alpha1 = 1
alpha2 = 1


class Project:
    def __init__(self, name, duration, score, best_before, roles):
        self.id = id(self)
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.roles = roles
        self.value = score/(alpha1 * len(self.roles) + alpha2 * duration)
        self.developers = []
        self.time_end = -1


class Developer:
    def __init__(self, name):
        self.id = id(self)
        self.name = name
        self.skills = dict()
        self.ocupation_time = 0


class Skill:
    def __init__(self, name, level):
        self.id = id(self)
        self.name = name
        self.level = level


class SuperDict(dict):
    def __init__(self, *arg, **kw):
        super(SuperDict, self).__init__(*arg, **kw)

    @staticmethod
    def build_key(skill_name: str, level: int):
        return f'{skill_name}#{level}'

    def ensure(self, key: str):
        if key not in self:
            self[key] = {'seniors': dict(), 'interns': dict()}

    def upgrade_level(self, developer: Developer, skill_name: str):
        current_level = developer.skills[skill_name].level
        next_key = self.build_key(skill_name, current_level + 1)
        if developer.name in self[next_key]['interns']:
            del self[next_key]['interns'][developer.name]
        self[next_key]['seniors'][developer.name] = developer
        next_next_key = self.build_key(skill_name, current_level + 2)
        self.ensure(next_next_key)
        self[next_next_key]['interns'][developer.name] = developer


def read_file(in_file):
    """
    Read Input File

    Args:
        in_file: input file path

    Returns:
        result_params: Resulted Parameters
    """
    # Define variables
    developers = []
    projects = []
    skills_lookup = dict()

    # Read the file into variables
    with open(in_file, 'r') as infile:
        super_dict = SuperDict()
        n_developers, n_projects = map(int, infile.readline().split(' '))
        for _ in range(n_developers):
            name, n_skills = infile.readline().split(' ')
            developer = Developer(name)
            for _ in range(int(n_skills)):
                skill_name, level = infile.readline().split(' ')
                skill_lookup_name = f'{skill_name}:{int(level)}'
                if skill_lookup_name not in skills_lookup:
                    skills_lookup[skill_lookup_name] = Skill(skill_name, int(level))
                developer.skills[skill_name] = skills_lookup[skill_lookup_name]
            developers.append(developer)
            for skill in developer.skills.values():
                for i in range(skill.level + 1):
                    key = SuperDict.build_key(skill.name, i)
                    super_dict.ensure(key)
                    super_dict[key]['seniors'][developer.name] = developer
                key = SuperDict.build_key(skill.name, skill.level + 1)
                super_dict.ensure(key)
                super_dict[key]['interns'][developer.name] = developer

        for _ in range(n_projects):
            name, duration, score, best_before, n_roles = infile.readline().split(' ')
            roles = []
            for _ in range(int(n_roles)):
                skill_name, level = infile.readline().split(' ')
                skill_lookup_name = f'{skill_name}:{int(level)}'

                if skill_lookup_name not in skills_lookup:
                    skills_lookup[skill_lookup_name] = Skill(skill_name, int(level))
                roles.append(skills_lookup[skill_lookup_name])
            projects.append(Project(name, int(duration), int(score), int(best_before), roles))

    return developers, projects, skills_lookup, super_dict


def select_as_random(proyect_list):
    return proyect_list.pop(rnd.randint(0, min([2, len(proyect_list)-1])))


def select_developer(proyect: Project, developers: List[Developer]):
    dev_list_roles = []
    for i in proyect.roles:
        dev_list = []
        for j in developers:
            if i.name not in j.skills.keys():
                j.skills[i.name] = Skill(i.name, 0)
            if j.skills[i.name].level >= i.level:
                dev_list.append(j)

        dev_list_roles.append(dev_list)

    for dev in dev_list_roles:
        lista = [i for i in dev if i not in proyect.developers]
        if len(lista) > 0:
            developer_selected = lista[rnd.randint(0, len(lista)-1)]
        else:
            break

        proyect.developers.append(developer_selected)

    if len(proyect.developers)==len(proyect.roles):
        proyect.time_end = max([i.ocupation_time for i in proyect.developers]) + proyect.duration
        for i in proyect.developers:
            i.ocupation_time += proyect.duration

        for i, role in enumerate(proyect.roles):
            j = proyect.developers[i]
            if j.skills[role.name].level == role.level:
                j.skills[role.name].level += 1


def copy_projects(projects: List[Project]) -> List[Project]:
    projects_c = []
    for p in projects:
        pc = copy.deepcopy(p)
        for d in p.developers:
            pc.developers.append(copy.deepcopy(d))
        projects_c.append(pc)

    return projects_c


def main_jf(in_file, out_file):
    developers_master, projects_master, skills_lookup, super_dict = read_file(in_file)
    sorted_projects_master = sorted(projects_master, key=lambda p: p.value, reverse=True)
    best_score = -1
    best_sol = None
    for _ in range(1):
        developers = copy.deepcopy(developers_master)
        sorted_projects = copy.deepcopy(sorted_projects_master)
        list_project = []
        while len(sorted_projects) > 0:
            proyect = select_as_random(sorted_projects)
            select_developer(proyect, developers)
            if len(proyect.developers) < len(proyect.roles):
                # sorted_projects.append(proyect)
                continue
            list_project.append(proyect)
        punt = 0
        for p in list_project:
            if p.time_end == -1:
                continue
            punt += p.score if p.time_end < p.best_before else max([p.score - (p.time_end - p.best_before), 0])
        if punt > best_score:
            best_score = punt
            best_sol = copy.deepcopy(list_project)
        # print(punt)

    print(f'Best punctuation: {best_score}')
    write_file(out_file, best_sol)


def dummy_solution(projects, developers, super_dict: SuperDict):
    """
    solution =
    {
        "project_name" : ["developer name]
    }
    """
    solution = dict()
    sorted_projects = sorted(projects, key=lambda p: p.value, reverse=True)
    while len(sorted_projects) > 0:
        project = sorted_projects.pop()
        solution[project.name] = set()
        for role in project.roles:
            super_name = SuperDict.build_key(role.name, role.level)
            super_dict.ensure(super_name)
            seniors = list(super_dict[super_name]['seniors'].values())

            for dev in seniors:
                if dev.name not in solution[project.name]:
                    solution[project.name].add(dev.name)
                    # increment skill level
                    if role.level == dev.skills[role.name].level:
                        super_dict.upgrade_level(dev, role.name)
                        dev.skills[role.name].level += 1

    return solution


def process(developers, projects, super_dict):
    """
    The main program reads the input file, processes the calculation
    and writes the output file

    Args:
        result_params: Resulted Parameters

    Returns:
        final_score: Final Score
        , final_result: Final Result
    """
    final_score = 0
    final_result = []

    ### Logic here
    final_result = dummy_solution(projects, developers, super_dict)

    return final_score, final_result  # return process result


def write_file(out_file, final_result: List[Project]):
    """
    Write the submission file

    Args:
        out_file: output file path
    """
    with open(out_file, 'w') as outfile:
        outfile.write(f'{len(final_result)}\n')
        for p in final_result:
            outfile.write(f'{p.name}\n')
            dev_names = [d.name for d in p.developers]
            outfile.write(f'{" ".join(dev_names)}\n')


def main(in_file, out_file):
    """
    The main program reads the input file, processes the calculation
    and writes the output file

    Args:
        in_file: input file path
        out_file: output file path
    """

    # Read File
    developers, projects, skills_lookup, super_dict = read_file(in_file)

    # Process Algorithm
    final_score, final_result = process(developers, projects, super_dict)

    # Print Score
    print('Score: {}'.format(final_score))

    # Save results into the output if instructed
    if out_file is not None:
        write_file(out_file, final_result)
        print('{} is saved. The program completed.'.format(out_file))
    else:
        print('The program completed.')


if __name__ == "__main__":
    # Check arguments
    main_jf('input_data/c_collaboration.in.txt', 'output_data/c_collaboration.out.txt')
    """
    if len(sys.argv) < 2:
        print(sys.argv[0] + ' [in file] [out file: optional]')
    elif len(sys.argv) == 2:
        main_jf(sys.argv[1], None)
    else:
        main_jf(sys.argv[1], sys.argv[2])
"""
### End of Program ###
