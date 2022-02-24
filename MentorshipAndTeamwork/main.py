import sys
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


class Developer:
    def __init__(self, name):
        self.id = id(self)
        self.name = name
        self.skills = dict()


class Skill:
    def __init__(self, name, level):
        self.id = id(self)
        self.name = name
        self.level = level


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
        super_dict = dict()
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
                    key = skill.name + str(i)
                    if key not in super_dict:
                        super_dict[key] = {
                            'interns': dict(),
                            'seniors': dict(),
                        }
                    super_dict[key]['seniors'][developer.name] = developer
                key = skill.name + str(skill.level + 1)
                if key not in super_dict:
                    super_dict[key] = {
                        'interns': dict(),
                        'seniors': dict(),
                    }
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


def dummy_solution(projects, developers, super_dict):
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
            super_name = f'{role.name}{role.level}'
            super_next_name = f'{role.name}{role.level + 1}'
            super_next_next_name = f'{role.name}{role.level + 2}'
            seniors = list(super_dict[super_name]['seniors'].values())

            for dev in seniors:
                if dev.name not in solution[project.name]:
                    solution[project.name].add(dev.name)
                    # increment skill level
                    if role.level == dev.skills[role.name].level:
                        dev.skills[role.name].level += 1
                        if super_next_name not in super_dict:
                            super_dict[super_next_name] = {'seniors': dict(), 'interns': dict()}

                        super_dict[super_next_name]['seniors'][dev.name] = dev
                        del super_dict[super_next_name]['interns'][dev.name]

                        if super_next_next_name not in super_dict:
                            super_dict[super_next_next_name] = {'seniors': dict(), 'interns': dict()}
                        super_dict[super_next_next_name]['interns'][dev.name] = dev

    return solution


def process(result_params):
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

    return final_score, final_result  # return process result


def write_file(out_file, final_result):
    """
    Write the submission file

    Args:
        out_file: output file path
    """
    with open(out_file, 'w') as outfile:
        # Save result into the output file
        pass


def main(in_file, out_file):
    """
    The main program reads the input file, processes the calculation
    and writes the output file

    Args:
        in_file: input file path
        out_file: output file path
    """

    # Read File
    result_params = read_file(in_file)
    # Process Algorithm
    final_score, final_result = process(result_params)
    # Print Score
    print('Score: {}'.format(final_score))
    # Save results into the output if instructed
    if out_file is not None:
        write_file(out_file, final_result)
        print('{} is saved. The program completed.'.format(out_file))
    else:
        print('The program completed.')


if __name__ == "__main__":
    developers, projects, skills_lookup, super_dict = read_file('input_data/a_an_example.in.txt')
    solution = dummy_solution(projects, developers, super_dict)
    print(solution)

    # # Check arguments
    # if len(sys.argv) < 2:
    #     print(sys.argv[0] + ' [in file] [out file: optional]')
    # elif len(sys.argv) == 2:
    #     main(sys.argv[1], None)
    # else:
    #     main(sys.argv[1], sys.argv[2])

### End of Program ###