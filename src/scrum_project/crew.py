from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
from dotenv import load_dotenv  # 📌 Importamos dotenv para leer el .env

# 🔥 Cargamos el archivo .env
load_dotenv()

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ScrumProject():
	"""ScrumProject crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def product_owner(self) -> Agent:
		return Agent(
			config=self.agents_config['product_owner'],
			allow_delegation=True,
			memory=True,
			verbose=True
		)

	@agent
	def scrum_master(self) -> Agent:
		return Agent(
			config=self.agents_config['scrum_master'],
			allow_delegation=True,
			memory=True,
			verbose=True
		)


	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	# Product Owner tasks
	@task
	def product_owner_research_analysis_design(self) -> Task:
		return Task(
			config=self.tasks_config['product_owner_research_analysis_design'],
		)

	@task
	def product_owner_create_specifications(self) -> Task:
		return Task(
			config=self.tasks_config['product_owner_create_specifications'],
			output_file='specifications.md'
		)

	@task
	def product_owner_create_user_stories(self) -> Task:
		return Task(
			config=self.tasks_config['product_owner_create_user_stories'],
			output_file='user_stories.md'
		)

	@task
	def product_owner_create_product_backlog(self) -> Task:
		return Task(
			config=self.tasks_config['product_owner_create_product_backlog'],
			output_file='product_backlog.md'
		)

	@task
	def product_owner_refine_backlog(self) -> Task:
		return Task(
			config=self.tasks_config['product_owner_refine_backlog'],
			output_file='refined_backlog.md'
		)
	
	# Scrum Master tasks
	@task
	def scrum_master_create_sprint_backlog(self) -> Task:
		return Task(
			config=self.tasks_config['scrum_master_create_sprint_backlog'],
			output_file='sprint_backlog.md'
		)

	@task
	def scrum_master_sprint_planning(self) -> Task:
		return Task(
			config=self.tasks_config['scrum_master_sprint_planning'],
			output_file='sprint_planning_doc.md'
		)

	@task
	def scrum_master_sprint_planning(self) -> Task:
		return Task(
			config=self.tasks_config['scrum_master_sprint_planning'],
			output_file='sprint_planning_doc.md'
		)

	@task
	def scrum_master_daily_scrum(self) -> Task:
		return Task(
			config=self.tasks_config['scrum_master_daily_scrum'],
			output_file='daily_scrum_doc.md'
		)

	@task
	def scrum_master_monitor_sprint(self) -> Task:
		return Task(
			config=self.tasks_config['scrum_master_monitor_sprint'],
			output_file='daily_scrum_doc.md'
		)

	@task
	def scrum_master_sprint_review(self) -> Task:
		return Task(
			config=self.tasks_config['scrum_master_sprint_review'],
			output_file='sprint_review_doc.md'
		)

	@task
	def scrum_master_sprint_retrospective(self) -> Task:
		return Task(
			config=self.tasks_config['scrum_master_sprint_retrospective'],
			output_file='sprint_retrospective_doc.md'
		)
	

	@crew
	def crew(self) -> Crew:
		"""Creates the ScrumProject crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			# process=Process.hierarchical,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
