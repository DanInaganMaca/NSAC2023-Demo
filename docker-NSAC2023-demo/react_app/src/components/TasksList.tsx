import { useEffect, useState } from "react"
import { getAllTasks } from "../api/tasks.api"
import { ITask } from "../models/task.model";
import { TaskCard } from "./TaskCard";

export function TasksList() {

  const [tasks, setTasks] = useState<ITask[]>([]);

  useEffect(() => {
    const loadTasks = async () => {
      const res = await getAllTasks();
      setTasks(res.data);
    }
    loadTasks();
  }, [])

  return (
    <div className="grid grid-cols-3 gap-3">
      {tasks.map((task: ITask) => (
        <TaskCard key={task.id} task={task} />
      ))}
    </div>
  )
} 
