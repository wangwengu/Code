import React, { Component } from 'react';

class Solution extends Component {
    state = {
        solutions: [
            {id: 1, title: "加工零件", views: 1},
            {id: 2, title: "加工零件", views: 2},
            {id: 3, title: "加工零件", views: 3},
            {id: 4, title: "加工零件", views: 4},
            {id: 5, title: "加工零件", views: 5},
            {id: 6, title: "加工零件", views: 6},
            {id: 7, title: "加工零件", views: 7},
            {id: 8, title: "加工零件", views: 8},
        ],
    };
    handleClickDelete = (solution) => {
        const solutions = this.state.solutions.filter(s => s !== solution);
        this.setState({
            solutions,
        });
    }
    render() { 
        return ((
            <table className="table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>标题</th>
                        <th>阅读量</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        this.state.solutions.map((solution) => (
                            <tr key={solution.id}>
                                <th>{solution.id}</th>
                                <td>{solution.title}</td>
                                <td>{solution.views}</td>
                                <td>
                                    <button type="button" onClick={() => this.handleClickDelete(solution)} className="btn btn-danger">删除</button>
                                </td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        ));
    }
}
 
export default Solution;
