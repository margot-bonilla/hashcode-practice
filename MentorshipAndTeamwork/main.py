import sys


class Project:
    def __init__(self, name, score, best_before):
        self.id = id(self)
        self.name = name
        self.score = score
        self.best_before = best_before
        self.roles = list()


class Developer:
    def __init__(self, name):
        self.id = id(self)
        self.name = name
        self.skills = list()


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
                developer.skills.append(skills_lookup[skill_lookup_name])
            developers.append(developer)
            for skill in developer.skills:
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
            name, days_to_complete, score, best_before, n_roles = infile.readline().split(' ')
            project = Project(name, int(score), int(best_before))
            for _ in range(int(n_roles)):
                skill, level = infile.readline().split(' ')
                skill_lookup_name = f'{skill_name}:{int(level)}'
                if skill_lookup_name not in skills_lookup:
                    skills_lookup[skill_lookup_name] = Skill(skill_name, int(level))
                project.roles.append(skills_lookup[skill_lookup_name])
            projects.append(project)

    return developers, projects, skills_lookup, super_dict


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
    read_file('input_data/a_an_example.in.txt')
    # # Check arguments
    # if len(sys.argv) < 2:
    #     print(sys.argv[0] + ' [in file] [out file: optional]')
    # elif len(sys.argv) == 2:
    #     main(sys.argv[1], None)
    # else:
    #     main(sys.argv[1], sys.argv[2])

### End of Program ###